import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import subprocess
import csv

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(PythonHighlighter, self).__init__(parent)
        
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)
        keywordFormat.setFontWeight(QFont.Bold)
        
        keywordPatterns = ["\\bFalse\\b", "\\bNone\\b", "\\bTrue\\b", "\\band\\b", "\\bas\\b", "\\bassert\\b",
                           "\\bbreak\\b", "\\bclass\\b", "\\bcontinue\\b", "\\bdef\\b", "\\bdel\\b", "\\belif\\b",
                           "\\belse\\b", "\\bexcept\\b", "\\bfinally\\b", "\\bfor\\b", "\\bfrom\\b", "\\bglobal\\b",
                           "\\bif\\b", "\\bimport\\b", "\\bin\\b", "\\bis\\b", "\\blambda\\b", "\\bnonlocal\\b",
                           "\\bnot\\b", "\\bor\\b", "\\bpass\\b", "\\braise\\b", "\\breturn\\b", "\\btry\\b",
                           "\\bwhile\\b", "\\bwith\\b", "\\byield\\b", "\\becho\\b"]
        
        self.highlightingRules = [(QRegExp(pattern), keywordFormat) for pattern in keywordPatterns]

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
    def __init__(self, online_ips):
        super().__init__()

        self.setWindowTitle("Adresses IP en ligne")
        self.online_ips = online_ips
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.checkbox_list = []

        for ip_data in self.online_ips:
            ip_checkbox = QCheckBox(ip_data['ip'])
            layout.addWidget(ip_checkbox)
            self.checkbox_list.append(ip_checkbox)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)

        self.setLayout(layout)

    def get_checked_ips(self):
        checked_ips = []
        for checkbox in self.checkbox_list:
            if checkbox.isChecked():
                checked_ips.append(checkbox.text())
        return checked_ips

class mon_editeur(QMainWindow):
    def __init__(self):
        super(mon_editeur, self).__init__()
        self.editor = CodeEditor() 
        self.fontSizeBox = QSpinBox()
        
        self.path = ""
        self.setCentralWidget(self.editor)
        self.setWindowTitle('Éditeur de code')
        self.resize(630,400)  
        self.create_tool_bar()
        
        style_file = QFile("../REMT/Tests/editeur_de_code/style.qss")
        style_file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(style_file)
        app.setStyleSheet(stream.readAll())
        
    def create_tool_bar(self):
        toolbar = QToolBar()
        
        openIcon = QIcon("../REMT/Tests/editeur_de_code/open.png")  
        openBtn = QPushButton(openIcon, 'Ouvrir', self)
        openBtn.clicked.connect(self.openFile)
        toolbar.addWidget(openBtn)
        
        saveIcon = QIcon("../REMT/Tests/editeur_de_code/save.png")  
        saveBtn = QPushButton(saveIcon, 'Sauvegarder', self)
        saveBtn.clicked.connect(self.saveFile)
        toolbar.addWidget(saveBtn)
        
        executeIcon = QIcon("../REMT/Tests/editeur_de_code/execute.png")  
        executeBtn = QPushButton(executeIcon, 'Exécuter Script Shell', self)
        executeBtn.clicked.connect(self.executeScript)
        toolbar.addWidget(executeBtn)

        showOnlineIPsBtn = QPushButton("Afficher les IP en ligne")
        showOnlineIPsBtn.clicked.connect(self.show_online_ips)
        toolbar.addWidget(showOnlineIPsBtn)

        self.addToolBar(toolbar)

    def executeScript(self):
        script = self.editor.toPlainText()
        if script:
            result = subprocess.run(["bash", "-c", script], capture_output=True, text=True)
            output = result.stdout.strip()
            error = result.stderr.strip()
            if output:
                QMessageBox.information(self, "Résultat de l'exécution", output)
            if error:
                QMessageBox.warning(self, "Erreur lors de l'exécution", error)
        else:
            QMessageBox.warning(self, "Aucun script", "Veuillez écrire un script dans l'éditeur.")

    def saveFile(self):
        print(self.path)
        if self.path == '':
            self.file_saves()
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)    
            
    def file_saves(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Enregistrer le fichier", "", "Documents texte (*.txt);Tous les fichiers (*)")
        if self.path == '':
            return   
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)    

    def openFile(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Documents texte (*.txt);Tous les fichiers (*)")
        if self.path == '':
            return
        try:
            with open(self.path, 'r') as f:
                text = f.read()
                self.editor.setPlainText(text)
                self.update_title()
        except Exception as e:
            print(e)

    def extract_online_ips(self, csv_path):
        online_ips = []
        try:
            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['online'].lower() == 'true':
                        online_ips.append({'ip': row['ip_add'], 'password': row['password'], 'linux_username': row['linux_username']})
        except Exception as e:
            print(e)
        return online_ips

    def show_online_ips(self):
      
        csv_path = "../REMT/Tests/editeur_de_code/snmp_users.csv"
        
        online_ips = self.extract_online_ips(csv_path)
        
        dialog = OnlineIPDialog(online_ips)
        if dialog.exec_():
            checked_ips = dialog.get_checked_ips()
            print("Adresses IP sélectionnées :", checked_ips)

app = QApplication(sys.argv)
window = mon_editeur()
window.show()
sys.exit(app.exec_())

# TODO:
     # CHANGE THE ICONS (YOU CAN FIND BETTER ONES IN \REMT\Tests\manager GUI tests)!!!
     # ADD ERROR HANDLING AND WARNINGS
     # CLEAN THE SCRIPT (REWRITE THE WHOLE THING IN ENGLISH)
    