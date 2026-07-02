import pandas


# Import CSV file and create a dataframe
data=pandas.read_csv("Day 26 NATO alphabet project/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

# Loop through dataframe and create new dict 
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Ask a word and create its list of letters
word=input("Enter a word: ").upper()

# Create a list with the phonetical words
phonetic_word_list=[data_dict[letter].title() for letter in word]
print(phonetic_word_list)