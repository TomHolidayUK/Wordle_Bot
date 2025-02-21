from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, 
    QHBoxLayout, QLabel, QLineEdit, QGroupBox, QFrame
)
from PyQt6.QtGui import QFont
from guess_calculator import best_guess

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wordle Bot")
        self.setGeometry(100, 100, 400, 200)
        
        self.main_layout = QVBoxLayout(self)

        # self.known_location_inputs = []
        # self.unknown_location_inputs = []

        self.known_location_inputs = ['a', '', 's', '', '']
        self.unknown_location_inputs = ['p']

        self.init_ui()

    def init_ui(self):

        print(self.known_location_inputs)
        print(self.unknown_location_inputs)
        
        title = QLabel("Add your letters so the bot can form its next guess")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)  # Change the font size
        title.setFont(font)
        self.main_layout.addWidget(title)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)  # Horizontal line
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(separator)

        label_known_location = QLabel("Letters with known location: ")
        self.main_layout.addWidget(label_known_location)

        h_layout = QHBoxLayout()

        for i in range(5):
            line_edit = QLineEdit(self.known_location_inputs[i])
            h_layout.addWidget(line_edit)
            self.known_location_inputs.append(line_edit)

        self.main_layout.addLayout(h_layout)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)  # Horizontal line
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(separator)

        self.main_layout.addWidget(QLabel("Add letters of unknown position:"))

        self.group_box = QGroupBox()
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)
        self.main_layout.addWidget(self.group_box)

        add_button_layout = QHBoxLayout()
        add_button_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        add_button_layout.setSpacing(0)  # Reduce spacing
        add_button = QPushButton("Add")
        add_button.setFixedWidth(100)
        add_button_layout.addWidget(add_button)
        add_button.clicked.connect(self.add_line)

        for letter in self.unknown_location_inputs:
            print(letter)
            #self.add_line(letter)
        
        self.group_box_layout.addLayout(add_button_layout)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)  # Horizontal line
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(separator)

        ready_button_layout = QHBoxLayout()
        ready_button = QPushButton("Ready!")
        ready_button.setFixedWidth(100)
        ready_button_layout.addWidget(ready_button)
        ready_button.clicked.connect(self.on_ready_button_clicked)
        self.main_layout.addLayout(ready_button_layout)

        self.setLayout(self.main_layout)

    def add_line(self):
        """Add a new QLineEdit for unknown location letters"""
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Letter with unknown location...")
        self.group_box_layout.addWidget(line_edit)
        self.unknown_location_inputs.append(line_edit)

    def on_ready_button_clicked(self):
        """Collect user inputs and print them"""
        known_letters = [line_edit.text() for line_edit in self.known_location_inputs]
        unknown_letters = [line_edit.text() for line_edit in self.unknown_location_inputs]

        print(f"Known location letters: {known_letters}")
        print(f"Unknown location letters: {unknown_letters}")

        self.known_location_inputs = known_letters
        self.unknown_location_inputs = unknown_letters

        self.clear_page()

        #guess = best_guess(known_letters, unknown_letters)
        guess = "salah"
        answer_label = QLabel(f"The bot's guess is: {guess}")
        answer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        answer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        next_guess_button_layout = QHBoxLayout()
        next_guess_button = QPushButton("next_guess!")
        next_guess_button.setFixedWidth(100)
        next_guess_button_layout.addWidget(next_guess_button)
        next_guess_button.clicked.connect(self.on_next_guess_button_clicked)
        self.main_layout.addWidget(answer_label)
        self.main_layout.addLayout(next_guess_button_layout)

    def on_next_guess_button_clicked(self):
        self.clear_page()
        self.init_ui()

    def clear_page(self):
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


# If run directly, start the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())