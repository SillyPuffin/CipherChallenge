from .utils import get_index
from .utils import alpha

def generate_lookup(aCo, bCo):
    lookup = {}
    for i in range(26):
        index = i * aCo
        index += bCo
        index %= 26
        lookup[index] = i
    
    return lookup


def BruteForceAffine(data,targets) -> list:
    datas = []
    for i in range(1,27,2):
        if i != 13:
            for x in range(26):
                newdata = ""
                #generate lookup table
                lookup = generate_lookup(i,x)

                for item in data:
                    index= get_index(item)
                    newindex= lookup[index]
                    newdata += alpha[newindex]
                datas.append((newdata,i,x))

    WordFoundAttempts = []
    for attempt in datas:
        word = attempt[0]
        for target in targets:
            if target in word:
                WordFoundAttempts.append((word,attempt[1],attempt[2]))
            
    return WordFoundAttempts