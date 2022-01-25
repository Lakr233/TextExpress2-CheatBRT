# get current script dir
import os
import sys

location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
words_file = os.path.join(location, 'words.txt')

# create words array
words = []
with open(words_file, 'r') as f:
    for line in f:
        words.append(line.strip().lower())

while True:
    # ask for input
    input_word = input('Enter a word: ').lower()
    if input_word == '':
        exit()
    result = []
    for w in words:
        if len(w) != len(input_word):
            continue
        # for all index of '_' in input_word
        match = True
        for i in range(len(input_word)):
            if input_word[i] == '_':
                continue
            if input_word[i] != w[i]:
                match = False
                break
        if match:
            result.append(w)
    if len(result) == 0:
        print('No match found')
    else:
        print('Found {} matches:'.format(len(result)))
        for r in result:
            print(r)
