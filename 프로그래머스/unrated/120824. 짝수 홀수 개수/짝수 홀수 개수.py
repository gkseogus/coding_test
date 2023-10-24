def solution(num_list):
    newL = [0, 0]
    
    for i in num_list:
        if(i % 2 == 0):
            newL[0] += 1
        else:
            newL[1] += 1
    
    return newL
           