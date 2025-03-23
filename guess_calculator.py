# Plan

# The aim is to create a bot that makes the best statistically-possible Wordle guesses
# By best statistically-possible guess, I mean a guess that uses the most common letters possible each time
# This will involve looping over a long list of possible words each time, I will try to optimise this performance
# Over time I hope this bot will yield impressive stats

# I have grabbed the 14885 words in the wordle word list from the Wordle source code (available via developer tools)

import json
from linguistic_tools import most_commonly_used_word, repeated_letters

import requests
from bs4 import BeautifulSoup


with open("all_words.json", "r") as file:
    all_words = json.load(file)

with open("possible_words.json", "r") as file:
    official_possible_words = json.load(file)


def scrape_previous_answers():
    url = "https://www.rockpapershotgun.com/wordle-past-answers"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select("ul.inline li")
        data = [item.get_text(strip=True) for item in items]
        return data
    else:
        print("Failed to fetch data")
        return []

previous_words = scrape_previous_answers()

# take previous worlde answers from word list to get possible words
possible_words = []
for word in official_possible_words:
    if word not in previous_words:
        possible_words.append(word)


# This map of letter frequency in the English dictionary is taken from https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
letter_frequency = {
    "E": 11.1607,
    "M": 3.0129,
    "A": 8.4966,
    "H": 3.0034,
    "R": 7.5809,
    "G": 2.4705,
    "I": 7.5448,
    "B": 2.0720,
    "O": 7.1635,
    "F": 1.8121,
    "T": 6.9509,
    "Y": 1.7779,
    "N": 6.6544,
    "W": 1.2899,
    "S": 5.7351,
    "K": 1.1016,
    "L": 5.4893,
    "V": 1.0074,
    "C": 4.5388,
    "X": 0.2902,
    "U": 3.6308,
    "Z": 0.2722,
    "D": 3.3844,
    "J": 0.1965,
    "P": 3.1671,
    "Q": 0.1962,
} 

letter_frequency_sorted = []

for i in range(26):
    highest_val = 0
    highest_letter = ""
    for letter in letter_frequency:
        current_val = float(letter_frequency[letter])
        if current_val > highest_val:
            highest_val = current_val
            highest_letter = letter

    letter_frequency_sorted.append([highest_letter.lower(), highest_val])
    del letter_frequency[highest_letter]

#print(letter_frequency_sorted)

starting_criteria =  {'b': '2', 'y': '5', 'a': 0} 
greens = ['', 'b', '', '', 'y']
yellows = ['a']
greys = ['e']
#abbey

def loop_all_words(exact_letters, available_letters, required_letters, allow_repetition):
    potential_guesses = []
    
    # loop through all possible words
    for word in possible_words:
        previous_letters = set()
        for i, char in enumerate(word):
            # first check aligns with known exact letters
            if i in exact_letters and exact_letters[i] != char and exact_letters[i] != "":
                break

            if char not in available_letters:
                break

            # check there's no unwanted letters - red letters
            if char in greys:
                break
  

            # check no repetition
            if not allow_repetition:
                if char in previous_letters:
                    break
                else:
                    previous_letters.add(char)

        # also check it includes required letters (where position is unknown)
        for required_letter in required_letters:
            if required_letter not in word:
                break
        
        # if we haven't found any guesses without repetition, try with
        potential_guesses.append(word)

    return potential_guesses


def find_matches(greens, yellows, greys, nots, allow_repetition):
    found_match = False
    not_possible = False
    common_letters = 0 # the number of most common letters to try 
    potential_guesses = []
    available_letters = []

    while not found_match and not_possible == False:

        exact_letters = dict() # letters where we know the exact position
        required_letters = set() # letters we know are part of the word (and so are required) but we don't know the position

        for letter in yellows:
            available_letters.append(letter)
            required_letters.add(letter)
        
        for i, letter in enumerate(greens):
            exact_letters[i] = letter

        for i in range(common_letters):
            if i == 26:
                print("no word found without repetition")
                not_possible = True
                break
            letter_to_add = letter_frequency_sorted[i][0]
            if letter_to_add not in available_letters:
                available_letters.append(letter_to_add)

        #print("available letters: ", available_letters)

        if not_possible:
            break

        # loop through all possible words
        for word in possible_words:
            possible = True
            previous_letters = set()
            for i, char in enumerate(word):
                # first check aligns with known exact letters
                if i in exact_letters and exact_letters[i] != char and exact_letters[i] != "":
                    possible = False
                    break

                if char not in available_letters:
                    possible = False
                    break

                # check there's no unwanted letters - red letters
                if char in greys:
                    possible = False
                    break   
                
                if not allow_repetition:
                    # check no repetition
                    if char in previous_letters:
                        possible = False
                        break
                    else:
                        previous_letters.add(char)

                # check that this letter is not in 'nots' - yellow at this location so therefore not here
                if len(nots[i]) != 0 and char in nots[i]:
                    possible = False
                    break

            # also check it includes required letters (where position is unknown)
            for required_letter in required_letters:
                if required_letter not in word:
                    possible = False
                    break

            # word is valid - add 
            if possible:
                potential_guesses.append(word)
                found_match = True

        common_letters += 1

    return potential_guesses


# find the best guess
def best_guess(greens, yellows, greys, nots):
    # we try to make a guess using the most common letters possible
    # we first try to find a guess without letter repetition, to maximise the chance of finding a letter rin the word
    # if this isn't possible we then try again with letter repetition   

    guesses = find_matches(greens, yellows, greys, nots, False)
    #print("guesses without repetition: ", guesses)

    if len(guesses) == 0:
        guesses = find_matches(greens, yellows, greys, nots, True)
        print("guesses with repetition: ", guesses)

    # worth evaluating which word most commonly appears in texts as this will be more likely to be a correct guess
    guesses_str = ""
    for guess in guesses:
        guesses_str += guess + ","

    return most_commonly_used_word(guesses_str)

