import requests 
import urllib 

# this function scrapes Google Ngram for json data to see which is the currently most commonly used word out of a det of words
def most_commonly_used_word(words, start_year=2021,  
             end_year=2022, corpus="en", 
             smoothing=0): 
  
    # converting a regular string to the standard URL format 
    words = urllib.parse.quote(words) 

    url = 'https://books.google.com/ngrams/json?content=' + words + '&year_start=' + str(start_year) + '&year_end=' + str(end_year) + '&corpus=' + str(corpus) + '&smoothing=' + str(smoothing) + '' 
  
    # requesting data from the above url 
    response = requests.get(url) 
  
    # extracting the json data  
    output = response.json() 
    return_data = [] 
  
    if len(output) == 0: 
        return "No data available for this Ngram."
    else: 
        for num in range(len(output)): 
            return_data.append((output[num]['ngram'],  
                                output[num]['timeseries'])  ) 
    
    most_common_word = "" 
    max_frequency = 0
    for data in return_data:
        if max(data[1]) > max_frequency:
            max_frequency = max(data[1])
            most_common_word = data[0]

    print(f"most common word is '{most_common_word}' with a frequency of {max_frequency}")

    return most_common_word

    



# check if a word has repeated letters - this is undesirable when guessing
def repeated_letters(word):
    all_letters = set()
    for letter in word:
        if letter in all_letters:
            return True
        else:
            all_letters.add(letter)
    return False