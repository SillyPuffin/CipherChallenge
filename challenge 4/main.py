import sys
import os
import math
from itertools import permutations

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import *

data = load_data("challenge 4/data.txt")
data = data.split(" ")
data = "".join(data)


# total = 0
# for i in range(LargestWidth):
#     comb = math.factorial(i+1)
#     total += comb
# print(f"total : {total}")

# data = data[0:41]
# for i in range(LargestWidth):
#     length = i + 1
#     column = transcription_columizer(length,data)
#     comb = math.factorial(length)
#     #print(comb)
#     array = [x+1 for x in range(length)]
#     combinationList = [list(tation) for tation in permutations(array,length)]
#     print(f"onto {length}")
#     for tation in combinationList:
#         solved = transcription_solver(data,tation)
#         solved = "".join(solved)
#         if solved[0:9] == target:
#             print(tation)