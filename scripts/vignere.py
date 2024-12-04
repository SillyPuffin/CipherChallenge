
#write a function that takes a letter
#finds the distance between every repeate of that letter
#lists multiples of those distances

#write a function that takes a distance and returns a letter every iteration of that distance

def LetterDistance(letterToCount,data):
    lastOccurenceIndex = 0
    distances = []
    for index, letter in enumerate(data):
        if letter == letterToCount:
            distances.append(index - lastOccurenceIndex)
            lastOccurenceIndex = index
    
    return distances

def returnStepLetters(step,data):
    s= ""
    for i in range(0,len(data),step):
        s += data[i].lower()
    
    return s