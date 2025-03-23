from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, 
    QHBoxLayout, QLabel, QLineEdit, QGroupBox, QFrame, QScrollArea
)
from PyQt6.QtGui import QFont, QPixmap
from guess_calculator import best_guess

import sys

class Letter(QLabel):
    def __init__(self, letter, parent=None):
        super().__init__(letter, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(50, 50) 

        self.setText(letter)
        self.update()  

        self.colors = ['transparent', 'green', 'yellow', 'grey']
        self.color_index = 0  
        self.current_color = self.colors[self.color_index]

        self.base_stylesheet = """
                font-size: 48px;
                font-weight: bold;
                font-family: 'Arial';
                color: white;
            """

        self.setStyleSheet(self.base_stylesheet + "background-color: transparent;")
        
        self.mousePressEvent = self.change_color

    def change_color(self, event):
        # Change the background color on click
        self.color_index = (self.color_index + 1) % len(self.colors)
        new_background = self.colors[self.color_index]
        self.current_color = self.colors[self.color_index]
        self.setStyleSheet(self.base_stylesheet + f"background-color: {self.current_color}; font-size: 36px;")
        self.update() 

    def get_color(self):
        return self.current_color 


class Word(QWidget):
    def __init__(self, word, parent=None):
        super().__init__(parent)
        
        layout = QHBoxLayout()

        word = word.ljust(5) # limit to 5 letters

        self.letters = []

        for item in word:
            letter = Letter(item)
            self.letters.append(letter)
            layout.addWidget(letter)

        self.setLayout(layout)

    def get_colors(self):
        return [letter.get_color() for letter in self.letters]

    def get_letters(self):
        return [letter.text() for letter in self.letters]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.greens = ['', '', '', '', '']
        self.yellows = []
        self.greys = []
        self.nots = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
        }

        self.setWindowTitle("Wordle Bot")
        self.setGeometry(100, 100, 400, 200)
        
        self.main_layout = QVBoxLayout(self)
        self.word_layout = QVBoxLayout(self)
        self.main_layout.addLayout(self.word_layout)

        initial_guess = best_guess(self.greens, self.yellows, self.greys, self.nots)
        word = Word(initial_guess.upper())
        self.word_layout.addWidget(word)

        guess_button = QPushButton("Guess!")
        self.main_layout.addWidget(guess_button)
        guess_button.clicked.connect(self.on_guess)

        # ADD ENTER KEYBOARD SHORTCUT


    def on_guess(self):
        for i in range(self.word_layout.count()):
            widget = self.word_layout.itemAt(i).widget()
            if isinstance(widget, Word):
                letters = widget.get_letters()
                colors = widget.get_colors() 
                for i in range(5):
                    if colors[i] == "green":
                        self.greens[i] = letters[i].lower()
                    elif colors[i] == "yellow":
                        self.yellows.append(letters[i].lower())
                        self.nots[i].add(letters[i].lower())
                    elif colors[i] == "grey":
                        self.greys.append(letters[i].lower())

        # print(self.greens)
        # print(self.yellows)
        # print(self.greys)
        print(self.nots)

        guess = best_guess(self.greens, self.yellows, self.greys, self.nots)
        print(guess)
        word = Word(guess.upper())
        self.word_layout.addWidget(word)

# If run directly, start the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())