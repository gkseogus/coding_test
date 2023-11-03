def solution(intStrs, k, s, l):
    newL = []
    newL2 = []
    
    for i in intStrs:
        newL.append(i[s:])
    for j in newL:
        if(int(j[:l]) > k):
            newL2.append(int(j[:l]))
        
    return newL2