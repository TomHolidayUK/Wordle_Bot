from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

# class SimpleUI(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("PyQt6 Basic UI")
#         self.setGeometry(100, 100, 300, 200)

#         self.layout = QVBoxLayout()
        
#         self.label = QLabel("Hello, PyQt6!")
#         self.layout.addWidget(self.label)

#         self.button = QPushButton("Click Me")
#         self.button.clicked.connect(self.on_click)
#         self.layout.addWidget(self.button)

#         self.setLayout(self.layout)

#     def on_click(self):
#         self.label.setText("Button Clicked!")

# app = QApplication([])
# window = SimpleUI()
# window.show()
# app.exec()

app = QApplication([])  # Create the application

def on_ready_button_clicked():
    # This function will be called when the button is clicked
    print("Ready button clicked!")
    # You can add more functionality here

window = QWidget()  # Create a main widget
window.setWindowTitle("Worlde Bot")
window.setGeometry(100, 100, 400, 100)

main_layout = QVBoxLayout()
h_layout = QHBoxLayout()

title = QLabel("Add your letters so the bot can form it's next guess")
main_layout.addWidget(title)

for i in range(1, 6):
    label = QLineEdit(f"")
    h_layout.addWidget(label)

main_layout.addLayout(h_layout)

ready_button = QPushButton("Ready")
main_layout.addWidget(ready_button)
ready_button.clicked.connect(on_ready_button_clicked)

window.setLayout(main_layout)  # Set the layout to the window
window.show()  # Show the window

app.exec()  # Start the application loop