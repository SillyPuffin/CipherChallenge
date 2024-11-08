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

def transcription_solver(data_set,width, code) -> list:
    newSet = []
    for row in data_set:
        indexes = [x for x in range(width)]
        for index in code:
            indexes.remove(index)

        s = ""
        for num in code:
            try:
                s += row[num]
            except IndexError:
                pass
        if len(code) < len(row):
            for item in indexes:
                s += row[item]
        newSet.append(s)
    return newSet