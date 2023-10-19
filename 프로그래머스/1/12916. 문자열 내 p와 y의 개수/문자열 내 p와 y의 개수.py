def solution(s):
    pcnt = 0
    ycnt = 0
    
    for i in s.upper():
        if(i == "P"):
            pcnt += 1
        if(i == 'Y'):
            ycnt += 1
            
    return True if(pcnt == ycnt) else False