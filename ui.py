from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox

app = QApplication([])  # Create the application

def on_ready_button_clicked(location_inputs):
    known_letters = [line_edit.text() for line_edit in location_inputs]
    #unknown_letters = letters_unknown_location.text()

    print(f"Known location letters: {known_letters}")
    #print(f"Unknown location letters: {unknown_letters}")

def add_line():
    # Create a new QLineEdit and add it to the group box layout
    new_line_edit = QLineEdit()
    new_line_edit.setPlaceholderText("Letter with unknown location...")
    group_box_layout.addWidget(new_line_edit)


window = QWidget()  # Create a main widget
window.setWindowTitle("Worlde Bot")
window.setGeometry(100, 100, 400, 100)

main_layout = QVBoxLayout()
h_layout = QHBoxLayout()

title = QLabel("Add your letters so the bot can form it's next guess")
main_layout.addWidget(title)

label_known_location = QLabel("Letters with known location: ")
h_layout.addWidget(label_known_location)

known_location_inputs = []

for i in range(1, 6):
    letters_known_location = QLineEdit(f"")
    h_layout.addWidget(letters_known_location)
    known_location_inputs.append(letters_known_location)

main_layout.addLayout(h_layout)

group_box = QGroupBox()
group_box_layout = QVBoxLayout()
group_box.setLayout(group_box_layout)
main_layout.addWidget(group_box)

add_button = QPushButton("Add")
add_button.clicked.connect(add_line)
group_box_layout.addWidget(add_button)

ready_button = QPushButton("Ready")
main_layout.addWidget(ready_button)
ready_button.clicked.connect(lambda: on_ready_button_clicked(known_location_inputs))

window.setLayout(main_layout)  # Set the layout to the window
window.show()  # Show the window

app.exec()  # Start the application loop
