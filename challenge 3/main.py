import sys,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import *

data = load_data("challenge 3/data.txt")
data = data.split(" ")
for index,item in enumerate(data):
    s = ""
    s += item[1:3]
    s += item[0]
    s += item[3]
    s += item[5]
    s += item[4]
    data[index] = s

print(data)
data = "".join(data)
print(data)