def solution(arr):
    newL = []
    
    for i in range(len(arr)):
        if(arr[i] == 2):
            newL.append(i)
    
    if(len(newL) == 0):
        return [-1]
    elif(len(newL) == 1):
        return [2]
    else:
        return arr[newL[0]:newL[-1] + 1]
        