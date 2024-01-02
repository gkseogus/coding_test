def solution(num_list):
    cnt = 0
    
    for i in num_list:
        num = i
        
        while (num != 1):
            if(num % 2 == 0):
                num /= 2
            else:
                num -= 1
                num /= 2
            cnt += 1
    
    return cnt