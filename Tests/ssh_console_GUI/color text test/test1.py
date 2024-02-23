import sys
from PyQt5.QtWidgets import QApplication, QTextEdit

def ansi_to_html(ansi_text):
    color_map = {
        '30': 'black',
        '31': 'red',
        '32': 'green',
        '33': 'yellow',
        '34': 'blue',
        '35': 'magenta',
        '36': 'cyan',
        '37': 'white'
    }
    html_text = ''
    in_escape = False
    current_code = ''
    for char in ansi_text:
        if char == '\x1b':
            in_escape = True
            current_code = ''
        elif in_escape:
            if char.isdigit():
                current_code += char
            elif char == ';':
                pass
            elif char.isalpha():
                if char == 'm':
                    if current_code in color_map:
                        html_text += f'<span style="color:{color_map[current_code]}">'
                    else:
                        html_text += '<span>'
                    current_code = ''
                    in_escape = False
        else:
            html_text += char
    return html_text

def main():
    app = QApplication(sys.argv)
    ansi_text = '\x1b[31mHello, \x1b[1mworld!\x1b[0m'
    html_text = ansi_to_html(ansi_text)
    text_edit = QTextEdit()
    text_edit.setHtml(html_text)
    text_edit.setAcceptRichText(False) 
    
    text_edit.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
