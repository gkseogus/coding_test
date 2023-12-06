def solution(n):
    newL = []  
    s = 2
    
    if(n == 2):
        return [2]
    
    while(s <= n):
        if(n % s == 0):
            newL.append(s)
            n = n / s
        else:
            s += 1
    
    return sorted(list(set(newL)))
                     