def load_data(path):
    with open(path,"r") as f:
        data = f.read()

    return data

def common(text):
    let_dict = {}
    for letter in text:
        if letter != " ":
            if letter in list(let_dict.keys()):
                let_dict[letter] += 1
            else:
                let_dict[letter] = 1

    max = 0
    mletter = ""
    for letter in let_dict:
        if let_dict[letter] > max:
            mletter = letter
            max = let_dict[letter]
    
    # print(let_dict)

    return mletter

def find_shift(first,second):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    firstindex = alpha.index(first)
    secondindex = alpha.index(second)
    return secondindex - firstindex

def transcription_columizer(columnSize,data) -> list: 
    count = 0
    columned = []
    s = ""
    for item in data:
        if count < columnSize:
            s += item
            count += 1
        else:
            columned.append(s)
            s = ""
            count = 1
            s += item

    columned.append(s)
    return columned

def transcription_solver(data_set, code) -> list:
    newSet = []
    for row in data_set:
        s = ""
        for num in code:
            try:
                s += row[num]
            except IndexError:
                pass
        newSet.append(s)
    return newSet
