file_path = 'books/frankenstein.txt'

with open(file_path) as f:
    file_contents = f.read()
    words = file_contents.split()
    print(len(words))