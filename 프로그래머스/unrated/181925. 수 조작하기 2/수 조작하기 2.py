def solution(numLog):
    newL = []
    for i in range(1, len(numLog)):
        nextIdx = numLog[i] - numLog[i-1]
        if(nextIdx == 1):
            newL.append('w')
        elif(nextIdx == -1):
            newL.append('s')
        elif(nextIdx == 10):
            newL.append('d')
        elif(nextIdx == -10):
            newL.append('a')
        elif(numLog[i] == 0):
            newL.append('w')
    return ''.join(newL)