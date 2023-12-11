def solution(n, m):
    answer = [0,0]
            
    for i in range(max(n,m), (n*m) + 1):
        if( i % n == 0 and i % m == 0):
            answer[1] = i
            break
            
    # 유클리드 호제법 최대공약수
    while m > 0:
        n, m = m, n % m
    answer[0] = n
    
    return answer