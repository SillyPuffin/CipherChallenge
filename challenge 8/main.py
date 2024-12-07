import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import *

data = load_data('challenge 8/numbers.txt')
data = data.split(' ')
data = ''.join(data)
data = data.lower()

pairs = [(f'{data[x]}{data[x+1]}') for x in range(0,int(len(data)/2),2)]

let_dict = {}
for pair in pairs:
    if pair != " ":
        if pair in list(let_dict.keys()):
            let_dict[pair] += 1
        else:
            let_dict[pair] = 1

ListedData = [(key,let_dict[key]) for key in let_dict]
ListedData = insertionSort(ListedData)

print(ListedData)

grid = {
    11:'g',
    21:'b',
    31:'u',
    41:'v',
    51:'m',
    12:'k',
    22:'w',
    32:'d',
    42:'r',
    52:'h',
    13:'y',
    23:'e',
    33:'a',
    43:'n',
    53:'l',
    14:'x',
    24:'p',
    34:'f',
    44:'j',
    54:'t',
    15:'i',
    25:'o',
    35:'s',
    45:'q',
    55:'c',
}

newstring = ''
for pair in pairs:
    if int(pair) in grid:
        newstring += grid[int(pair)]
    else:
        newstring += pair

print(newstring)

def find_factors(num) -> list:
    """finds all the factors of a number"""
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors

print(len(newstring))
print(find_factors(len(newstring)))