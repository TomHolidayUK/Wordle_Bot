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

        self.colours = ['transparent', 'green', 'yellow', 'grey']
        self.colour_index = 0  
        self.current_colour = self.colours[self.colour_index]

        self.base_stylesheet = """
                font-size: 48px;
                font-weight: bold;
                font-family: 'Arial';
                color: white;
            """

        self.setStyleSheet(self.base_stylesheet + "background-color: transparent;")
        
        self.mousePressEvent = self.change_colour

    def change_colour(self, event):
        # Change the background colour on click
        self.colour_index = (self.colour_index + 1) % len(self.colours)
        new_background = self.colours[self.colour_index]
        self.current_colour = self.colours[self.colour_index]
        self.setStyleSheet(self.base_stylesheet + f"background-color: {self.current_colour}; font-size: 36px;")
        self.update() 

    def get_colour(self):
        return self.current_colour 


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

    def get_colours(self):
        return [letter.get_colour() for letter in self.letters]

    def get_letters(self):
        return [letter.text() for letter in self.letters]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.greens = ['', '', '', '', '']
        self.yellows = set()
        self.greys = set()
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
        self.word_layout = QVBoxLayout()
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
                colours = widget.get_colours() 
                for i in range(5):
                    if colours[i] == "green":
                        self.greens[i] = letters[i].lower()
                    elif colours[i] == "yellow":
                        self.yellows.add(letters[i].lower())
                        self.nots[i].add(letters[i].lower())
                    elif colours[i] == "grey":
                        self.greys.add(letters[i].lower())

        guess = best_guess(self.greens, self.yellows, self.greys, self.nots)
        word = Word(guess.upper())
        self.word_layout.addWidget(word)

# If run directly, start the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())