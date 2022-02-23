# A left rotation operation on an array

def rotateLeft(d, arr):
    for i in range(d):
        poped = arr.pop(0)
        arr.append(poped)
    return arr
