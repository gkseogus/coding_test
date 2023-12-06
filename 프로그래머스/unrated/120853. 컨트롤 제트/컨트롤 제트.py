def solution(s):
    newL = []
    splitL = s.split()
    
    for i in range(len(splitL)):
        if(splitL[i] == 'Z'):
            newL.append(int(splitL[i-1]) * (-1))
        else:
            newL.append(int(splitL[i]))
    
    return sum(newL)