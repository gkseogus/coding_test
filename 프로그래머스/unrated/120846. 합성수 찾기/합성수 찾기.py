def solution(n):
    newL = []
    cnt = 0
    
    for i in range(4, n + 1):
        for j in range(1, i + 1):
            if(i % j == 0):
                newL.append(i)    
        if(newL.count(i) > 2):
            cnt += 1
    
    return cnt