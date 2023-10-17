def solution(n):
    newL = []
    
    while n != 1:
        if(len(newL) == 0):
            n = n
        elif(n % 2 == 0):
            n = n // 2
        else:
            n = 3 * n + 1
        newL.append(n)
    return newL