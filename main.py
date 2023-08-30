import string
file_path = 'books/frankenstein.txt'

with open(file_path) as f:
    file_contents = f.read()
    words = file_contents.split()

    # create a dict to store letters and number times each on appears
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}

    for letter in file_contents.lower():
        if letter in letter_counts:
            letter_counts[letter] += 1
    
    print(letter_counts)
