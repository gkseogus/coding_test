def solution(arr, divisor):
    newL = []
    
    for i in arr:
        if(i % divisor == 0):
            newL.append(i)
    
    if(len(newL) == 0):
        return [-1]
    else:
        return sorted(newL)