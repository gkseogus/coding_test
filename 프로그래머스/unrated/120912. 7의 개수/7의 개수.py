def solution(array):
    cnt = 0
    
    for i in list(''.join(map(str, array))):
        if(i == "7"):
            cnt += 1
            
    return cnt