import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import *

numbers = load_data('challenge 7/numbers.txt')
letters = load_data('challenge 7/data.txt')

numbers = numbers.split(' ')
numbers = ''.join(numbers)

letters = letters.split(' ')
letters = ''.join(letters)

pairs = []
for i in range(len(letters)):
    letter = letters[i]
    number = numbers[i]
    pairs.append((letter,number))

letterstox = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4
}

numberstoy = {
    '1':0,
    '2':1,
    '3':2,
    '4':3,
    '5':4
}

finished_string = ''
alpha = 'abcdefghijklmnopqrstuvwxy'

for pair in pairs:
    x = letterstox[pair[0]]
    y = numberstoy[pair[1]]

    #convert x y to 1d index
    index = 5 * x + y
    finished_string += alpha[index]

print(finished_string)