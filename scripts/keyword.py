def swapLetters(String, SwapList):
    #generate individual letter list with a zero to check if changed
    newString  = [(letter, 0) for letter in String]

    for item in SwapList:
        for index,letter in enumerate(newString):
            if letter[0] == item[0] and letter[1] == 0:
                newString[index] = (item[1],1)

    joinedString = ''
    for let in newString:
        joinedString += let[0]
    

    return joinedString