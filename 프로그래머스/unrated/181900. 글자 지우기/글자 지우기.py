def solution(my_string, indices):
    newL = list(my_string)
    
    for i in indices:
        newL[i] = ''
    return ''.join(newL)