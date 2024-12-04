import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import *

data = load_data('challenge 5/data2.txt')
data = data.split(" ")

data = "".join(data)

#data1
#common are e :337 and t:261 multiple 1,2,3,6,19,23


# for i in get_multiple(len(data)):
#     print(i)

# newdata = []
# s = ""
# for letter in range(len(data)):
#     s += data[letter]
#     if len(s) == 6:
#         newdata.append(s)
#         s = ""

# for triplet in newdata:
#     print(triplet)

# columns = transcription_columizer(6, data)
# solved = transcription_solver(columns, 6, [4,5,3,1,0,2])
# solved = "".join(solved)
# print(solved)

##data 2
#H is most common followed by E:   E -> H : T -> E
#print(common(data))

# print(LetterDistance('E',data))

steppedData = returnStepLetters(4,data)

print(steppedData)

print(common(steppedData)[0])
shift = find_shift("e",common(steppedData)[0][0])

newSteppedDate = ""
for letter in steppedData:
    index = get_index(letter)
    
    #remove shift
    index -= shift
    #do modulus to ensure its not out of bounds e.g -3 = 23
    index += 26
    index %= 26
    newSteppedDate += alpha[index]

print(newSteppedDate)