def solution(d, budget):
    newL = []
    cnt = 0
    
    for i in sorted(d):
        cnt += i
        if(cnt > budget):
            break
        else:
            newL.append(i)
    
    return len(newL)
    