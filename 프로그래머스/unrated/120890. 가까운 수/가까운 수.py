def solution(array, n):
    newL = []
    array.sort()
    
    for i in array:
        if(n-i < 0):
            newL.append((n - i) * -1)
        else:
            newL.append(n - i)

    return array[newL.index(min(newL))]