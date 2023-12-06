def solution(s):
    newD = {}
    newL = []
    
    for i in s:
        if(i in newD):
            newD[i] = 2
        else:
            newD[i] = 1
    
    for idx,val in newD.items():
        if(val == 1):
            newL.append(idx)
            
    return ''.join(sorted(newL))