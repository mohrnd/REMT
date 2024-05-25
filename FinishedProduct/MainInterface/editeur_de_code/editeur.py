import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import subprocess
import csv
import os
from .transfert import Transfer
import platform
import tempfile
from qfluentwidgets import  PushButton, PasswordLineEdit, CheckBox, PrimaryPushButton
from .cipher_decipher_logic.AES_cipher_decipher import get_password_no_form

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

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)
        
class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)

    def lineNumberAreaWidth(self):
        digits = 1
        max_ = max(1, self.blockCount())
        while max_ >= 10:
            max_ /= 10
            digits += 1
        space = 3 + self.fontMetrics().width('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(Qt.black)
                rect = QRect(0, int(top), self.lineNumberArea.width(), self.fontMetrics().height())
                painter.drawText(rect, Qt.AlignRight, number)


            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

    def highlightCurrentLine(self):
        extraSelections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()

            lineColor = QColor(Qt.yellow).lighter(160)

            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)

        self.setExtraSelections(extraSelections)

class OnlineIPDialog(QDialog):
    def __init__(self, online_ips, current_file_path):
        super().__init__()

        self.setWindowTitle("Online IP Addresses")
        self.online_ips = online_ips
        self.current_file_path = current_file_path
        self.password_entered = None 
        self.setFixedWidth(300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.checkbox_list = []
        transfer = Transfer()

        for ip_data in self.online_ips:
            ip_checkbox = CheckBox(ip_data['ip'])
            layout.addWidget(ip_checkbox)
            self.checkbox_list.append(ip_checkbox)
            
        # Add the Masterpassword_input field
        self.master_password_input = PasswordLineEdit(self)
        self.master_password_input.setEchoMode(PasswordLineEdit.Password)  # Set the input to password mode
        self.master_password_input.setPlaceholderText("Master password")
        layout.addWidget(self.master_password_input)

        send_button = PrimaryPushButton("SEND")
        send_button.clicked.connect(self.send_files)
        layout.addWidget(send_button)

        cancel_button = PrimaryPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        layout.addWidget(cancel_button)

        self.setLayout(layout)
        
        # Connect the signal to update the master password variable
        self.master_password_input.textChanged.connect(self.update_master_password)
        
    
    def update_master_password(self, text):
        self.password_entered = text

    def send_files(self):
        password_entered = self.password_entered
        if not password_entered:
            QMessageBox.warning(self, "Warning", "Please enter a password.")
            return
        
        

        checked_ips = [checkbox.text() for checkbox in self.checkbox_list if checkbox.isChecked()]
        if not checked_ips:
            QMessageBox.warning(self, "No IP address selected", "Please select at least one IP address.")
            return

        if not self.current_file_path:
            QMessageBox.warning(self, "File not saved", "Please save the file first before sending it.")
            return

        local_path = self.current_file_path
        remote_path = "./" + os.path.basename(local_path)

        success_ips = []
        for ip in checked_ips:
            for ip_data in self.online_ips:
                if ip_data['ip'] == ip:
                    username = ip_data['linux_username']
                    ciphered_password = ip_data['password']
                    password1 = get_password_no_form(password_entered,ciphered_password)
                    password=password1
                    result = Transfer.PUT(ip, username, password, local_path, remote_path)
                    print(result)
                    success_ips.append(ip)
                    break

        # if success_ips:
        #     success_message = "The file was successfully sent to the following IP addresses :\n" + "\n".join(
        #         success_ips)
        #     QMessageBox.information(self, "File sent", success_message)

class CodeEditorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.editor = CodeEditor()
        self.fontSizeBox = QSpinBox()

        self.highlighter = PythonHighlighter(self.editor.document())

        self.path = ""
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)

        # Charger le fichier de style CSS
        style_file = QFile("../REMT/Tests/editeur_de_code/style.qss")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            self.setStyleSheet(stream.readAll())
            style_file.close()
        else:
            print("Impossible d'ouvrir le fichier de style CSS.")
        
class MainWindowWidget(QWidget):
    def __init__(self):
        super(MainWindowWidget, self).__init__()
        self.editorWidget = CodeEditorWidget() 
        self.currentFilePath = None  # Variable pour stocker le chemin du fichier actuellement ouvert
        self.path = "" 
        self.create_tool_bar()
        
        self.editor = self.editorWidget.editor  # Accès à l'éditeur de code à partir de editorWidget
        
        self.setFixedSize(820,850) 
        # Changer le style de la classe MainWindowWidget
        self.setStyleSheet("background-color: #1a1a1a; color: white;")

    
    def create_tool_bar(self):
    
        toolbar = QToolBar()
        
        # Styling the toolbar
        toolbar.setStyleSheet("""
            QToolBar {
                background-color: #1a1a1a; 
                color: white; 
                border: 1px solid #1a1a1a;
                                    }
        """)
        
        toolbar.addSeparator(),toolbar.addSeparator()
        
        newIcon = QIcon("../REMT/Tests/editeur_de_code/new.png")  
        newBtn = PushButton(newIcon, 'New', self)
        newBtn.clicked.connect(self.newFile)
        # self.applyButtonStyle(newBtn)  # Appliquer le style au bouton New
        newBtn.setFixedSize(100, 30)
        toolbar.addWidget(newBtn)
        
        toolbar.addSeparator(),toolbar.addSeparator()

        
        openIcon = QIcon("../REMT/Tests/editeur_de_code/open.png")  
        openBtn = PushButton(openIcon, 'Open', self)
        openBtn.clicked.connect(self.openFile)
        # self.applyButtonStyle(openBtn)  
        openBtn.setFixedSize(100, 30)
        toolbar.addWidget(openBtn)
        
        toolbar.addSeparator(),toolbar.addSeparator()
        
        
        saveIcon = QIcon("../REMT/Tests/editeur_de_code/save.png")  
        saveBtn = PushButton(saveIcon, 'Save', self)
        saveBtn.clicked.connect(self.saveFile)
        # self.applyButtonStyle(saveBtn) 
        saveBtn.setFixedSize(120, 30)
        toolbar.addWidget(saveBtn)
        
        toolbar.addSeparator(),toolbar.addSeparator()
        
        executeIcon = QIcon("../REMT/Tests/editeur_de_code/execute.png")  
        executeBtn = PushButton(executeIcon, 'Verify Shell', self)
        executeBtn.clicked.connect(self.verifier_shell_script) 
        # self.applyButtonStyle(executeBtn) 
        executeBtn.setFixedSize(120, 30)
        toolbar.addWidget(executeBtn)
        
        toolbar.addSeparator(),toolbar.addSeparator()
        
        verifyPythonIcon = QIcon("../REMT/Tests/editeur_de_code/Python.png")  
        verifyPythonBtn = PushButton(verifyPythonIcon, 'Verify Python', self)
        verifyPythonBtn.clicked.connect(self.verifier_python_script)
        # self.applyButtonStyle(verifyPythonBtn) 
        verifyPythonBtn.setFixedSize(140, 30)
        toolbar.addWidget(verifyPythonBtn)
        
        toolbar.addSeparator(),toolbar.addSeparator()
    

        sendIcon = QIcon("../REMT/Tests/editeur_de_code/Send.png")
        showOnlineIPsBtn = PushButton( sendIcon,'Send File',self)
        showOnlineIPsBtn.clicked.connect(self.show_online_ips)
        # self.applyButtonStyle(showOnlineIPsBtn) 
        showOnlineIPsBtn.setFixedSize(120, 30)
        toolbar.addWidget(showOnlineIPsBtn)
        
        

        # Ajoutez la barre d'outils directement à la fenêtre principale
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        self.setLayout(layout)
        
        # Ajouter l'éditeur de code après la barre d'outils
        layout.addWidget(self.editorWidget)
        
        
        

        
    def closeEvent(self, event):
            # Vérifier s'il y a des modifications non sauvegardées dans l'éditeur de code
            if self.editorWidget.editor.document().isModified():
                # Afficher une boîte de dialogue pour demander à l'utilisateur s'il veut sauvegarder les modifications
                response = QMessageBox.question(self, "Unsaved Changes", "Do you want to save your changes before closing?", QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
                if response == QMessageBox.Save:
                    self.saveFile()
                elif response == QMessageBox.Cancel:
                    # Annuler la fermeture de la fenêtre si l'utilisateur choisit d'annuler
                    event.ignore()
                    return
            
            # Si aucune modification non sauvegardée ou si l'utilisateur choisit de continuer sans sauvegarder, fermer la fenêtre
            event.accept()
            
            

        
    def set_current_file_path(self, file_path):
        self.currentFilePath = file_path

    def get_current_file_path(self):
        return self.currentFilePath

    def get_path(self):
        return self.path
    
    def set_path(self, path):
        self.path = path


    def saveFile(self):
        if self.get_path() == '':
            self.path, _ = QFileDialog.getSaveFileName(self, "Enregistrer le fichier", "", "Scripts Shell (*.sh);;Scripts Python (*.py);;Fichiers texte (*.txt)")
            if self.path == '':
                return   
        text = self.editorWidget.editor.toPlainText()  # Accès à l'éditeur de code via editorWidget
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.setWindowTitle(f'Éditeur de code - {os.path.basename(self.path)}') 
                self.set_current_file_path(self.path)  # Définir le chemin du fichier actuellement ouvert
                self.set_path(self.path)  # Mettre à jour le chemin du fichier
        except Exception as e:
            print(e)



    def newFile(self):
        self.path = ""
        self.editorWidget.editor.clear()  # Accès à l'éditeur de code via editorWidget
        self.setWindowTitle('Éditeur de code') 
        self.set_current_file_path("")  # Mettre à jour le chemin du fichier actuellement ouvert avec une chaîne vide


    def openFile(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Scripts Shell (*.sh);;Scripts Python (*.py);;Fichiers texte (*.txt)")
        if self.path == '':
            return
        try:
            with open(self.path, 'r') as f:
                text = f.read()
                self.editorWidget.editor.setPlainText(text)  # Accéder à l'éditeur de code via editorWidget
                self.setWindowTitle(f'Éditeur de code - {os.path.basename(self.path)}') 
                self.set_current_file_path(self.path)  # Définir le chemin du fichier actuellement ouvert
                self.set_path(self.path)  # Mettre à jour le chemin du fichier
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
            csv_path = "machines.csv"
            online_ips = self.ping_online_ips(csv_path)
            dialog = OnlineIPDialog(online_ips, self.path)
            self.password_entered = None 
            dialog.exec_()
                    
    
    
    def verifier_python_script(self):
        
        script_content = self.editorWidget.editor.toPlainText().split('\n')[:10]  # Accès à l'éditeur de code via editor

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

        script_content = self.editorWidget.editor.toPlainText().split('\n')[:10]  # Accès à l'éditeur de code via editorWidget

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



# app = QApplication(sys.argv)
# window = MainWindowWidget()
# window.show()
# sys.exit(app.exec_())

