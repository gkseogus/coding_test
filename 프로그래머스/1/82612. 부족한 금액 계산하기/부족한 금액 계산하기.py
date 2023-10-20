def solution(price, money, count):
    cnt = 0
    
    for i in range(1, count + 1):
            cnt += price * i
    
    if(money > cnt):
        return 0
    else:
        return (cnt - money) 