import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import subprocess
import csv
import os
from transfert import Transfer
import platform
import tempfile

def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname} > NUL 2>&1")
    if response == 0:
        return True  
    else:
        return False 
class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(PythonHighlighter, self).__init__(parent)
        
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)
        keywordFormat.setFontWeight(QFont.Bold)
        
        printFormat = QTextCharFormat()
        printFormat.setForeground(QColor("#B03060"))  # Rose foncé pour le mot-clé print
        
        dollarFormat = QTextCharFormat()
        dollarFormat.setForeground(Qt.darkBlue)  # Orange pour le caractère $
        
        keywordPatterns = ["\\bFalse\\b", "\\bNone\\b", "\\bTrue\\b", "\\band\\b", "\\bas\\b", "\\bassert\\b",
                           "\\bbreak\\b", "\\bclass\\b", "\\bcontinue\\b", "\\bdef\\b", "\\bdel\\b", "\\belif\\b",
                           "\\belse\\b", "\\bexcept\\b", "\\bfinally\\b", "\\bfor\\b", "\\bfrom\\b", "\\bglobal\\b",
                           "\\bif\\b", "\\bimport\\b", "\\bin\\b", "\\bis\\b", "\\blambda\\b", "\\bnonlocal\\b",
                           "\\bnot\\b", "\\bor\\b", "\\bpass\\b", "\\braise\\b", "\\breturn\\b", "\\btry\\b",
                           "\\bwhile\\b", "\\bwith\\b", "\\byield\\b", "\\becho\\b"]
        
        self.highlightingRules = [(QRegExp(pattern), keywordFormat) for pattern in keywordPatterns]

        self.highlightingRules.append((QRegExp("\\bprint\\b"), printFormat))  # Ajout de la règle pour le mot-clé print
        self.highlightingRules.append((QRegExp("\\$"), dollarFormat))  # Ajout de la règle pour le caractère $

        self.commentStartExpression = QRegExp("#")
        self.commentEndExpression = QRegExp("$")

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.darkGreen)

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)
            commentLength = 0
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()
            self.setFormat(startIndex, commentLength, self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text, startIndex + commentLength)

class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        
        self.highlighter = PythonHighlighter(self.document())

class OnlineIPDialog(QDialog):
    def __init__(self, online_ips, current_file_path):
        super().__init__()

        self.setWindowTitle("Online IP Addresses")
        self.online_ips = online_ips
        self.current_file_path = current_file_path
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.checkbox_list = []
        transfer = Transfer()

        for ip_data in self.online_ips:
            ip_checkbox = QCheckBox(ip_data['ip'])
            layout.addWidget(ip_checkbox)
            self.checkbox_list.append(ip_checkbox)

        send_button = QPushButton("SEND")
        send_button.clicked.connect(self.send_files)
        layout.addWidget(send_button)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)

        self.setLayout(layout)

    def send_files(self):
        checked_ips = [checkbox.text() for checkbox in self.checkbox_list if checkbox.isChecked()]
        if not checked_ips:
            QMessageBox.warning(self, "No IP address selected", "Please select at least one IP address.")
            return

        if not self.current_file_path:
            QMessageBox.warning(self, "File not saved", "Please save the file first before sending it.")
            return

        local_path = self.current_file_path  
        remote_path = "/home/user2/Bureau/" + os.path.basename(local_path)
                            #change it by: "/etc/remt" + os.path.basename(local_path)

        success_ips = []
        for ip in checked_ips:
            for ip_data in self.online_ips:
                if ip_data['ip'] == ip:
                    username = ip_data['linux_username']
                    password = ip_data['password']
                    result = Transfer.PUT(ip, username, password, local_path, remote_path)
                    print(result)
                    success_ips.append(ip)
                    break

        if success_ips:
            success_message = "The file was successfully sent to the following IP addresses :\n" + "\n".join(success_ips)
            QMessageBox.information(self, "File sent", success_message)

class mon_editeur(QMainWindow):
    def __init__(self):
        super(mon_editeur, self).__init__()
        self.editor = CodeEditor() 
        self.fontSizeBox = QSpinBox()
        
        self.path = ""
        self.setCentralWidget(self.editor)
        self.setWindowTitle('Éditeur de code')
        self.resize(560,400)  
        self.setFixedSize(self.size()) 
        self.create_tool_bar()
        
        style_file = QFile("../REMT/Tests/editeur_de_code/style.qss")
        style_file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(style_file)
        app.setStyleSheet(stream.readAll())
        
    def create_tool_bar(self):
        toolbar = QToolBar()
        
        newIcon = QIcon("../REMT/Tests/editeur_de_code/new.png")  
        newBtn = QPushButton(newIcon, 'New', self)
        newBtn.clicked.connect(self.newFile)
        toolbar.addWidget(newBtn)
        
        openIcon = QIcon("../REMT/Tests/editeur_de_code/open.png")  
        openBtn = QPushButton(openIcon, 'Open', self)
        openBtn.clicked.connect(self.openFile)
        toolbar.addWidget(openBtn)
        
        saveIcon = QIcon("../REMT/Tests/editeur_de_code/save.png")  
        saveBtn = QPushButton(saveIcon, 'Save', self)
        saveBtn.clicked.connect(self.saveFile)
        toolbar.addWidget(saveBtn)
        
        executeIcon = QIcon("../REMT/Tests/editeur_de_code/execute.png")  
        executeBtn = QPushButton(executeIcon, 'Verify Shell', self)
        executeBtn.clicked.connect(self.verifier_shell_script) 
        toolbar.addWidget(executeBtn)
        
        verifyPythonIcon = QIcon("../REMT/Tests/editeur_de_code/python.png")  
        verifyPythonBtn = QPushButton(verifyPythonIcon, 'Verify Python', self)
        verifyPythonBtn.clicked.connect(self.verifier_python_script)
        toolbar.addWidget(verifyPythonBtn)

        sendIcon = QIcon("../REMT/Tests/editeur_de_code/send.png")
        showOnlineIPsBtn = QPushButton( sendIcon,'Send File',self)
        showOnlineIPsBtn.clicked.connect(self.show_online_ips)
        toolbar.addWidget(showOnlineIPsBtn)
        



        self.addToolBar(toolbar)



    def saveFile(self):
        if self.path == '':
            self.path, _ = QFileDialog.getSaveFileName(self, "Enregistrer le fichier", "", "Scripts Shell (*.sh);;Scripts Python (*.py);;Fichiers texte (*.txt)")
            if self.path == '':
                return   
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.setWindowTitle(f'Éditeur de code - {os.path.basename(self.path)}') 
        except Exception as e:
            print(e)

    def newFile(self):
        self.path = ""
        self.editor.clear()
        self.setWindowTitle('Éditeur de code')

    def openFile(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Scripts Shell (*.sh);;Scripts Python (*.py);;Fichiers texte (*.txt)")
        if self.path == '':
            return
        try:
            with open(self.path, 'r') as f:
                text = f.read()
                self.editor.setPlainText(text)
                self.setWindowTitle(f'Éditeur de code - {os.path.basename(self.path)}') 
        except Exception as e:
            print(e)


    def ping_online_ips(self, csv_path):
            online_ips = []
            try:
                with open(csv_path, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        ip = row['ip_add']
                        is_online = Check_ip(ip)  
                        if is_online: 
                            online_ips.append({
                                'ip': ip,
                                'password': row['password'],
                                'linux_username': row['linux_username']
                            })
            except Exception as e:
                print(e)
            return online_ips

    def show_online_ips(self):
            csv_path = "../REMT/Tests/editeur_de_code/snmp_users.csv"
            online_ips = self.ping_online_ips(csv_path)
            dialog = OnlineIPDialog(online_ips, self.path)
            dialog.exec_()
                    
    
    
    def verifier_python_script(self):
        
        script_content = self.editor.toPlainText().split('\n')[:10]  

        is_python_script = any(line.startswith("#!/usr/bin/env python") or line.startswith("#!/usr/bin/python") for line in script_content)

        if is_python_script:  
            
            try:
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
                temp_file.write(self.editor.toPlainText().encode())
                temp_file.close()
                self.temp_file_path = temp_file.name

                process = subprocess.Popen(["python", self.temp_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()

                if stderr:
                    QMessageBox.warning(self, "Error running Python script", stderr)
                else:
                    QMessageBox.information(self, "Script execution successful", "The Python script is correct.")
            except Exception as e:
                QMessageBox.warning(self, "Erreur", f"An error has occurred : {str(e)}")
            finally:
                if self.temp_file_path:
                    os.unlink(self.temp_file_path)

            
        else:
            QMessageBox.warning(self, "Vérification Python", "The script does not appear to be a Python script. Make sure it starts with: \n\n #!/usr/bin/env python \n\n ou \n\n #!/usr/bin/python")

    
    def verifier_shell_script(self):

        script_content = self.editor.toPlainText().split('\n')[:10]  

        is_shell_script = any(line.startswith("#!/bin/bash") or line.startswith("#!/bin/sh") for line in script_content)

        if is_shell_script: 
            try:
                
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".sh")
                temp_file.write(self.editor.toPlainText().encode())
                temp_file.close()
                self.temp_file_path = temp_file.name

                if platform.system() == 'Windows':
                    programfiles = ('PROGRAMW6432' if platform.architecture()[0] == '32bit'
                                    else 'PROGRAMFILES')
                    bash_exe = os.getenv(programfiles) + r'\Git\bin\bash'

                    process = subprocess.Popen([bash_exe, self.temp_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    stdout, stderr = process.communicate()

                    
                    if stderr:
                        QMessageBox.warning(self, "Error running Python script", stderr)
                    else:
                        QMessageBox.information(self, "Script execution successful", "The SHELL script is correct.")
            except Exception as e:
                QMessageBox.warning(self, "Erreur", f"An error has occurred : {str(e)}")
            finally:
                if self.temp_file_path:
                    os.unlink(self.temp_file_path)
        else:
            QMessageBox.warning(self, "Vérification Shell", "The script does not appear to be a SHELL script. Make sure it starts with: \n\n #!/bin/bash \n\n ou \n\n #!/bin/sh")


app = QApplication(sys.argv)
window = mon_editeur()
window.show()
sys.exit(app.exec_())
