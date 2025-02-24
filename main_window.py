from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, 
    QHBoxLayout, QLabel, QLineEdit, QGroupBox, QFrame
)
from PyQt6.QtGui import QFont
from guess_calculator import best_guess

import sys

class MainWindow(QWidget):
    def __init__(self, known_location, unknown_locations, unwanted):
        super().__init__()
        print("init - ", known_location, unknown_locations, unwanted)
        self.setWindowTitle("Wordle Bot")
        self.setGeometry(100, 100, 400, 200)
        
        self.main_layout = QVBoxLayout(self)

        self.init_ui(known_location, unknown_locations, unwanted)

    def init_ui(self, known_location, unknown_locations, unwanted):

        self.known_location_inputs = known_location
        self.unknown_location_inputs = unknown_locations
        self.unwanted_letters = unwanted

        # self.known_location_inputs = ['a', '', 's', '', '']
        # self.unknown_location_inputs = ['p', 'r']
        # self.unwanted_letters = ['c', 'h']

        self.letter_list = LetterList("Unwanted Letters", self.unwanted_letters)

        print(self.known_location_inputs)
        print(self.unknown_location_inputs)
        
        title = QLabel("Add your letters so the bot can form its next guess")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)  # Change the font size
        title.setFont(font)
        self.main_layout.addWidget(title)

        separator = Separator()
        self.main_layout.addWidget(separator)

        label_known_location = QLabel("Letters with known location: ")
        self.main_layout.addWidget(label_known_location)

        h_layout = QHBoxLayout()

        for i in range(5):
            line_edit = QLineEdit(self.known_location_inputs[i])
            h_layout.addWidget(line_edit)
            self.known_location_inputs.append(line_edit)

        self.main_layout.addLayout(h_layout)

        separator = Separator()
        self.main_layout.addWidget(separator)

        self.main_layout.addWidget(QLabel("Add letters of unknown position:"))

        self.group_box = QGroupBox()
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)
        self.main_layout.addWidget(self.group_box)

        add_button_layout = QHBoxLayout()
        add_button_layout.setContentsMargins(0, 0, 0, 0)  
        add_button_layout.setSpacing(0)  
        add_button = QPushButton("Add")
        add_button.setFixedWidth(100)
        add_button_layout.addWidget(add_button)
        add_button.clicked.connect(lambda: self.add_line())

        for i in range(len(self.unknown_location_inputs)):
            letter = self.unknown_location_inputs[i]
            self.add_line(letter)  
        self.group_box_layout.addLayout(add_button_layout)

        separator = Separator()
        self.main_layout.addWidget(separator)

        # Need to add letters that are NOT in the word, add this as an object - LetterList
        label = "Add letters that are not in the word: "
        self.main_layout.addWidget(self.letter_list)

        ready_button_layout = QHBoxLayout()
        ready_button = QPushButton("Ready!")
        ready_button.setFixedWidth(100)
        ready_button_layout.addWidget(ready_button)
        ready_button.clicked.connect(self.on_ready_button_clicked)
        self.main_layout.addLayout(ready_button_layout)

        self.setLayout(self.main_layout)

    def add_line(self, input=""):
        """Add a new QLineEdit for unknown location letters"""
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Letter with unknown location...")
        line_edit.setText(input)  
        self.group_box_layout.addWidget(line_edit)
        self.unknown_location_inputs.append(line_edit)

    def on_ready_button_clicked(self):
        """Collect user inputs and print them"""
        known_letters = [
            line_edit.text() for line_edit in self.known_location_inputs if isinstance(line_edit, QLineEdit)
        ]
        unknown_letters = [
            line_edit.text() for line_edit in self.unknown_location_inputs if isinstance(line_edit, QLineEdit)
        ]
        unwanted_letters = [
            line_edit.text() if isinstance(line_edit, QLineEdit) else str(line_edit)
            for line_edit in self.unwanted_letters
        ]

        print(f"Known location letters: {known_letters}")
        print(f"Unknown location letters: {unknown_letters}")
        print(f"Unwanted letters: {unwanted_letters}")

        self.known_location_inputs = known_letters
        self.unknown_location_inputs = unknown_letters
        self.unwanted_letters = unwanted_letters

        self.clear_page()

        guess = best_guess(known_letters, unknown_letters, unwanted_letters)
        #guess = "words"

        self.answer_label = QLabel(f"The bot's guess is: {guess}")
        self.answer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.answer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.next_guess_button_layout = QHBoxLayout()
        self.next_guess_button = QPushButton("next_guess!")
        self.next_guess_button.setFixedWidth(100)
        self.next_guess_button_layout.addWidget(self.next_guess_button)

        self.next_guess_button.clicked.connect(self.on_next_guess_button_clicked)

        self.main_layout.addWidget(self.answer_label)
        self.main_layout.addLayout(self.next_guess_button_layout)

    def on_next_guess_button_clicked(self):
        self.clear_page()
        self.init_ui(self.known_location_inputs, self.unknown_location_inputs, self.unwanted_letters) 

    def clear_page(self):
        print("clear_page")
         # Remove current widget features
        for i in reversed(range(self.main_layout.count())):
            item = self.main_layout.itemAt(i)
        
            if item is None:
                continue
            
            widget = item.widget()
            layout = item.layout()
            
            if widget is not None:
                widget.deleteLater()
                self.main_layout.removeWidget(widget)
            
            # If it's a layout, clear and remove it
            elif layout is not None:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()
                self.main_layout.removeItem(layout)


class Separator(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.Shape.HLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)

class LetterList(QWidget):
    def __init__(self, label="", unwanted_letters=None):
        super().__init__()
        self.unwanted_letters = unwanted_letters
        self.list_layout = QVBoxLayout()
        self.list_layout.addWidget(QLabel(label))

        self.group_box = QGroupBox()
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)
        self.list_layout.addWidget(self.group_box)

        add_button_layout = QHBoxLayout()
        add_button_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        add_button_layout.setSpacing(0)  # Reduce spacing
        add_button = QPushButton("Add")
        add_button.setFixedWidth(100)
        add_button_layout.addWidget(add_button)
        add_button.clicked.connect(lambda: self.add_line2())

        self.group_box_layout.addLayout(add_button_layout)

        # for i in range(len(self.unknown_location_inputs)):
        #     if isinstance(self.unknown_location_inputs[i], QLineEdit):  
        #         self.add_line(self.unknown_location_inputs[i].text())  
        # self.group_box_layout.addLayout(add_button_layout)

        self.setLayout(self.list_layout)

    def add_line2(self, input=""):
        print("input: ", input)
        """Add a new QLineEdit for unknown location letters"""
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Letter with unknown location...")
        line_edit.setText(input)  
        self.group_box_layout.addWidget(line_edit)
        self.unwanted_letters.append(line_edit)


# If run directly, start the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())