def solution(a, b):
    cnt = 0
    
    if(a > b):
        for i in range(b, a + 1):
            cnt += i
    else:
        for j in range(a, b + 1):
            cnt += j
    return cnt