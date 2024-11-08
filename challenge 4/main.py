import sys
import os
import math
from itertools import permutations

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import *

data = load_data("challenge 4/data2.txt")
data = data.split(" ")
data = "".join(data)


###part B
data = data.lower()
data= data[0:50]

successful = BruteForceAffine(data,['charles','ada','warne'])
print(successful)


####part A
#letter = common(data)
#print(f"E: {letter[0][0]}, T: {letter[1][0]}\n")


# #MRCHARLESBABBAGEDORSETSTREETMARYLEBONELONDON

# width = 24

# columned = transcription_columizer(width,data)

# solved = transcription_solver(columned,width, [3,4,2,5,1,0,9,6,8,15,7,10,11,12,14,17,13,16,21,18])

# for i in range(15):
#     print(solved[i])