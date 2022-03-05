"""Co-occurrence.py Find line of words indicated by user.

Program will take input of file name from user, check that filename exists
and raise error if it does not. The program will read the file and write
all contents to dictionary. While or before writing to dictionary, program
will convert all characters to lowercase, split the line into words,
remove all punction, apostrophes, and hyphens. Program will also remove
words with less than two characters. Program will write these lines to
dictionary. Then program will take input words from user and search the
dictionary for them, displaying the line numbers where each word is found
to the user.
"""


import string


def open_file(file_name):
    """Open file that was input."""
    # open file_name
    user_file = open(file_name)
    return user_file


def read_data(user_file):
    """Process and read the file."""
    # Set empty dictionary
    D = {}
    # Set count to 1
    line_count = 1
    # read file line by line
    data = user_file.readlines()
    for line in data:
        # Remove leading spaces and newline character
        line = line.strip()
        # Rewrite in lowercase
        line = line.lower()
        # Remove punctuation
        line = line.strip(string.punctuation)
        # Remove commas
        line = line.replace(",", "")
        # Remove hyphen
        line = line.replace("-", "")
        # Remove apostrophe
        line = line.replace("'", "")
        # Split line into words
        words = line.split(" ")
        for word in words:
            # Remove words smaller than 2 letters
            if len(word) < 2:
                continue
            # Remove words containing non-letters
            if not word.isalpha():
                continue
            # check if key is in dict already
            if word in D and line_count not in D.get(word):
                # sets value:key pair
                D[word] = D.get(word).union(set([line_count]))
                continue
            else:
                D[word] = set([line_count])
                # line_count += 1
                continue
        line_count += 1
    return D


def find_cooccurrence(D, words):
    """Find words in both variables."""
    # splits variable words into list called find_these
    find_these = words.split(" ")
    # searches dictionary for the input words
    sorted_list = set()
    # compare the lists display words on both lists
    for word in find_these:
        if word not in D:
            print("No co-occurence!")
            return
        else:
            # add first element to set
            if len(sorted_list) == 0:
                sorted_list.update(D[word])
                print(",".join(str(e) for e in sorted_list))


def main():
    """Handle I/O."""
    print("Hello User! If you give me a file name I will then prompt you\
 to tell me some words. I will tell you on what line(s) those words can\
 be found.")
    while True:
        try:
            file_name = input("Please type your file name and press\
 ENTER:")
            # call open_file and pass in the file name
            user_file = open_file(file_name)
            break
        except:
            print("File not found, please try again!")
    # call read_data and pass in the file returned by open_file
    D = read_data(user_file)
    while True:
        words = input("Please type words that you would like to search\
 for seperated by a space, then press ENTER, or q to quit:")
        if words == "q" or words == "Q":
            print("Goodbye!")
            user_file.close()
            break
        else:
            find_cooccurrence(D, words)


if __name__ == "__main__":
    main()
