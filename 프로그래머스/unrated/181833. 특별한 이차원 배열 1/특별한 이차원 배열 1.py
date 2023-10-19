def solution(n):
    newL = []
    for i in range(n):
        line = []
        for j in range(n):
            if(i == j):
                line.append(1)
            else:
                line.append(0)
        newL.append(line)
    return newL