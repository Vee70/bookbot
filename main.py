import string

def get_letter_counts(text):
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    for letter in text.lower():
        if letter in letter_counts:
            letter_counts[letter] += 1
    return letter_counts


file_path = 'books/frankenstein.txt'

with open(file_path) as f:
    file_contents = f.read()

total_words = len(file_contents.split())

letter_counts = get_letter_counts(file_contents)
letter_counts = list(letter_counts.items())
letter_counts.sort(key=lambda x: x[1], reverse=True)
    
print(f'--- Begin report of {file_path} ---')
print(f'{total_words} words found in the document\n')
for letter, counts in letter_counts:
    print(f"The '{letter}' character was found {counts} times")
print(f'--- End report ---')
