import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QCheckBox


# This template works !!!!
class SyncedTextEditsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.text_edits = []
        self.checkboxes = []

        for _ in range(4):
            text_edit = QTextEdit()
            checkbox = QCheckBox("Enabled")
            checkbox.setChecked(True)

            self.text_edits.append(text_edit)
            self.checkboxes.append(checkbox)

            layout.addWidget(text_edit)
            layout.addWidget(checkbox)

        self.setLayout(layout)
        self.setWindowTitle('Synced Text Edits Widget')

    def keyPressEvent(self, event):
        key = event.text()
        for text_edit, checkbox in zip(self.text_edits, self.checkboxes):
            if checkbox.isChecked():
                text_edit.insertPlainText(key)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SyncedTextEditsWidget()
    widget.show()
    sys.exit(app.exec_())
