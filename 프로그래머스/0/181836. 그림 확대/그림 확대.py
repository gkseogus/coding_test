def solution(picture, k):
    newL = []

    for i in picture:
        row = ''
        
        for j in i:
            row += j * k 
        
        for t in range(k):
            newL.append(row)
            
    return newL
