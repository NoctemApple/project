import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

def main():
    app = QApplication(sys.argv)
    win = QDialog()

    # MORSE AREA

    text_area = QTextEdit(win)
    text_area.setGeometry(50, 20, 300, 80)
    text_area.setPlaceholderText("Click buttons to insert text...")
    text_area.setReadOnly(True) 

    # Shows Cursor
    text_area.setFocusPolicy(Qt.StrongFocus)
    text_area.setTextInteractionFlags(Qt.TextSelectableByKeyboard)
    text_area.setFocus()
    
    # TRANSLATION AREA

    tl_area = QTextEdit(win)
    tl_area.setGeometry(50, 120, 300, 80)
    tl_area.setReadOnly(True)

    # TOOLTIP

    tip = QPushButton("?", win)
    tip.setGeometry(15, 10, 20, 20)
    tip.setToolTip("Single space for letters\nTriple space for words")
    tip.setEnabled(False)
    tip.setStyleSheet("""
    QPushButton {
        background-color: #0082FC;
        color: white;
        border: 0px solid black; 
        border-radius: 10px; 
        font-weight: bold;
        font-size: 12px;
    } """)

    # BUTTONS

    b1 = QPushButton(win)
    b1.setText(".")
    b1.setGeometry(200, 150, 100, 40)
    b1.move(50, 210)
    b1.clicked.connect(lambda: handle_button_click(text_area, b1.text()))

    b2 = QPushButton(win)
    b2.setText("-")
    b2.setGeometry(200, 150, 100, 40)
    b2.move(150, 210)
    b2.clicked.connect(lambda: handle_button_click(text_area, b2.text()))

    b3 = QPushButton(win)
    b3.setText("Space")
    b3.setGeometry(200, 150, 100, 40)
    b3.move(250, 210)
    b3.clicked.connect(lambda: handle_button_click(text_area, " "))

    b4 = QPushButton("Clear", win)
    b4.setGeometry(50, 150, 100, 40)
    b4.move(50, 250)
    b4.clicked.connect(lambda: handle_backspace(text_area))

    b5 = QPushButton(win)
    b5.setText("Clear All")
    b5.setGeometry(200, 150, 100, 40)
    b5.move(150, 250)
    b5.clicked.connect(lambda: clear_all(text_area, tl_area))

    b6 = QPushButton(win)
    b6.setText("Translate")
    b6.setGeometry(200, 150, 100, 40)
    b6.move(250, 250)
    b6.clicked.connect(lambda: translator(text_area, tl_area))

    # WINDOW

    win.setGeometry(100, 100, 400, 300)
    win.setFixedSize(400, 300)
    win.setWindowTitle("Morse Code Simulator by Noctem")
    win.setStyleSheet("""
    QDialog {
        background-color: black;
    } """)
    win.show()
    sys.exit(app.exec_())

# BUTTON CLICK HANDLER

# BUTTON CLICK HANDLER
space_count = 0  # Counter for consecutive spaces

def handle_button_click(text_area, text):
    global space_count
    cursor = text_area.textCursor()
    cursor.movePosition(cursor.End)
    text_area.setTextCursor(cursor)

    if text == " ":
        space_count += 1
        if space_count == 3:
            # Remove the last two spaces and replace them with "/"
            current_text = text_area.toPlainText()
            if len(current_text) >= 2 and current_text[-2:] == "  ":
                text_area.setPlainText(current_text[:-2] + "/")
                cursor.movePosition(cursor.End)
                text_area.setTextCursor(cursor)
            space_count = 0
        else:
            text_area.insertPlainText(" ")
    else:
        space_count = 0  # Reset counter if it's not a space
        text_area.insertPlainText(text)

def handle_backspace(text_area):
    current_text = text_area.toPlainText()
    if current_text:
        text_area.setPlainText(current_text[:-1])
        cursor = text_area.textCursor()
        cursor.movePosition(cursor.End)
        text_area.setTextCursor(cursor)


def clear_all(text_area, tl_area):
    text_area.clear()
    tl_area.clear()

def translator(text_area, tl_area):

    # MORSE DICTONARY

    morse = {
    '.-'    : 'A', '-...'   : 'B', '-.-.'   : 'C', '-..'    : 'D', '.'      : 'E', 
    '..-.'  : 'F', '--.'    : 'G', '....'   : 'H', '..'     : 'I', '.---'   : 'J', 
    '-.-'   : 'K', '.-..'   : 'L', '--'     : 'M', '-.'     : 'N', '---'    : 'O', 
    '.--.'  : 'P', '--.-'   : 'Q', '.-.'    : 'R', '...'    : 'S', '-'      : 'T', 
    '..-'   : 'U', '...-'   : 'V', '.--'    : 'W', '-..-'   : 'X', '-.--'   : 'Y', 
    '--..'  : 'Z',

    '.----' : '1', '..---'  : '2', '...--'  : '3', '....-'  : '4', '.....'  : '5', 
    '-....' : '6', '--...'  : '7', '---..'  : '8', '----.'  : '9', '-----'  : '0',

    '--..--': ',', '.-.-.-' : '.', '..--..' : '?', '.----.' : "'", '-.-.--' : '!',
    '-..-.' : '/', '-.--.'  : '(', '-.--.-' : ')', '.-...'  : '&', '---...' : ':', 
    '-.-.-.': ';', '-...-'  : '=', '.-.-.'  : '+', '-....-' : '-', '..--.-' : '_', 
    '.-..-.': '"', '...-..-': '$', '.--.-.' : '@', '/'      : ' ' }
    
    # MORSE TRANSLATOR
    
    morse_text = text_area.toPlainText().strip()

    words = morse_text.split("/")
    translated_words = []

    for word in words:

        letters = word.split()
        translated_letters = ''.join(morse.get(code, '?') for code in letters)
        translated_words.append(translated_letters)

    translated_text = ' '.join(translated_words)
    tl_area.setPlainText(translated_text)


if __name__ == "__main__":
    main()
