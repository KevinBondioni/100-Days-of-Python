import pandas


# Import CSV file and create a dataframe
data=pandas.read_csv("Day 26 NATO alphabet project/nato_phonetic_alphabet.csv")

# Loop through dataframe and create new dict 
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def word_list():
    # Ask a word and create its list of letters
    word=input("Enter a word: ").upper()
    try:
        phonetic_word_list=[data_dict[letter].title() for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")       
        word_list()
    else:
        print(phonetic_word_list)

word_list()


