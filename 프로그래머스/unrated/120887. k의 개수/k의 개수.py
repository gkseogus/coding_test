def solution(i, j, k):
    newL = []
    cnt = 0
    
    for i in range(i, j + 1):
        newL.append(i)
    
    for i in list(''.join(map(str, (newL)))):
        if(i == str(k)):
            cnt += 1
    
    return cnt