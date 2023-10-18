def solution(s):
    cnt = 0
    ans = True
    newL = list(s)
    
    for i in range(0, len(newL)):
        if(newL[i] == "("):
            cnt += 1
        else:
            cnt -= 1
        
        if(cnt < 0):
            return False
        
    if(cnt > 0):
        return False
    else:
        return True
