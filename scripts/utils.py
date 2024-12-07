alpha = "abcdefghijklmnopqrstuvwxyz"

def load_data(path):
    with open(path,"r") as f:
        data = f.read()

    return data

def insertionSort(arr):
    """sorts a tuple list based on the value of the second number"""
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key[1] < arr[j][1]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
    arr.reverse()
    return arr

def common(text):
    let_dict = {}
    for letter in text:
        if letter != " ":
            if letter in list(let_dict.keys()):
                let_dict[letter] += 1
            else:
                let_dict[letter] = 1

    ListedData = [(key,let_dict[key]) for key in let_dict]
    ListedData = insertionSort(ListedData)
    
    # print(let_dict)

    return ListedData

def get_index(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return alpha.index(letter)

def find_shift(first,second):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    firstindex = alpha.index(first)
    secondindex = alpha.index(second)
    return secondindex - firstindex




