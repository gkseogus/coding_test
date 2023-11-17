def solution(array):
    newL = []
    
    for idx, val in enumerate(array):
        if(max(array) == val):
            newL.append(val)
            newL.append(idx)
    
    return newL