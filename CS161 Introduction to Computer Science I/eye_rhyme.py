"""Eye_rhyme.py find word in dictionary with same last three letters.

Program will compare the last three letters of a user-input word with the
last three letters of every word in dictionary.txt, print out a list of
all matching words.
"""


# Start here
def eye_rhyme():
    """Take input from user, compare to dictionart to find matches."""
    # Open dictionary file
    dictionary = open("dictionary.txt", "r")
    # Take input word from user
    input_word = input("Please enter what word you would like to use,\
 then press ENTER:")
    # Seperates the last three letters of the input word
    last_letters_input = input_word[-3:len(input_word)]
    # Seperates each word into a list
    dictionary_list = dictionary.readlines()
    # Loop to compare and print words if they match/eye rhyme
    for word in dictionary_list:
        # Seperates the last three letters of each dictionary word, minus
        # the new line designator.
        last_letters_word = word[-4:len(word)-1]
        # print(last_letters_word)
        # print(last_letters_input)
        # If the last three letters of each word match, print the word.
        if last_letters_input == last_letters_word:
            print(word)


print("Hello User! I will take an input word that you give me and find\
 words that eye rhyme with that word. Eye rhyme is when the last three\
 letters match.")
eye_rhyme()
