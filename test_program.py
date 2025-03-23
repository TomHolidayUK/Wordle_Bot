# This script is designed to test the accuracy of the wordle bot

import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont

import json
import random
import time

from guess_calculator import best_guess

with open("possible_words.json", "r") as file:
    possible_words = json.load(file)

NUMBER_OF_TESTS = 500

guess_distribution = {
    6: 0,
    5: 0,
    4: 0,
    3: 0,
    2: 0,
    1: 0
}

max_streak = 0
current_streak = 0 
fails = 0

def compare_result(result, target):
    greens = ['', '', '', '', '']
    yellows = set()
    greys = set()
    nots = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
    }
    for i in range(5):
        if result[i] == target[i]:
            greens[i] = result[i]
        else:
            if result[i] in target:
                yellows.add(result[i])
                nots[i].add(result[i])
            else:
                greys.add(result[i])

    return (greens, yellows, greys, nots)
        

def update_stats(amount):
    global current_streak, max_streak, guess_distribution
    if amount > 0 and amount < 6:
        guess_distribution[amount] += 1
        current_streak += 1
        max_streak = max(max_streak, current_streak)


for i in range(NUMBER_OF_TESTS):
    greens = ['', '', '', '', '']
    yellows = set()
    greys = set()
    nots = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
    }

    target = random.choice(possible_words)
    print(f"Test number {i}. Searching for {target}")

    found = False
    attempts = 0

    while attempts < 6:
        guess = best_guess(greens, yellows, greys, nots)
        attempts += 1

        if guess == target:
            print(f"Found {target} in {attempts} attempts")
            update_stats(attempts)
            found = True
            break

        (new_greens, new_yellows, new_greys, new_nots) = compare_result(guess, target)

        for i in range(5):
            if new_greens[i] != '':
                greens[i] = new_greens[i]
            
        yellows.update(new_yellows)

        greys.update(new_greys)

        for key, value in new_nots.items():
            if len(value) == 1:
                nots[key].add(next(iter(value)))
            elif len(value) > 1:
                nots[key].update(value)

    if not found:
        print("FAIL")
        fails += 1
        update_stats(0)

    # need delay to circumvent google ngram request rate limit
    delay = 4
    time.sleep(delay)

win_percentage =  ((NUMBER_OF_TESTS - fails) / NUMBER_OF_TESTS) * 100.0
print(guess_distribution)
print(win_percentage)
print(max_streak)

def open_stats(data):
    attempts = []
    frequencies = []

    for attempt, frequency in data.items():
        attempts.append(attempt)
        frequencies.append(frequency)

    figure, ax = plt.subplots(figsize=(6, 4))
    ax.barh(attempts, frequencies, color='skyblue')
    ax.invert_yaxis()
    ax.set_title('Guess Distribution')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('No. of Attempts')

    return figure

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Wordle Bot Stats')
layout = QVBoxLayout()
stats_layout = QHBoxLayout()

def create_stat_layout(value, text):
    layout = QVBoxLayout()

    stat_label = QLabel(str(value))
    stat_label.setAlignment(Qt.AlignCenter)
    stat_label.setFont(QFont("Arial", 16, QFont.Bold))  
    
    text_label = QLabel(text)
    text_label.setAlignment(Qt.AlignCenter)
    text_label.setFont(QFont("Arial", 12))  
    
    layout.addWidget(stat_label)
    layout.addWidget(text_label)
    
    return layout

stats_layout.addLayout(create_stat_layout(NUMBER_OF_TESTS, "Played"))
stats_layout.addLayout(create_stat_layout(win_percentage, "Win %"))
stats_layout.addLayout(create_stat_layout(max_streak, "Max Streak"))

layout.addLayout(stats_layout)

figure = open_stats(guess_distribution)
canvas = FigureCanvas(figure)
layout.addWidget(canvas)
window.setLayout(layout)
window.resize(600, 400)
window.show()
sys.exit(app.exec_())


failures = ["krill", "woozy","dopey"]