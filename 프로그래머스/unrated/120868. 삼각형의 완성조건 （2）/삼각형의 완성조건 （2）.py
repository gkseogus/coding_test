def solution(sides):
    newL = []
    
    # 가장 긴 변인 경우
    for i in range(1, max(sides) + 1):
        if(min(sides) + i > max(sides)):
            newL.append(i)
            
    # 나머지 한 변이 가장 긴 변인 경우            
    for i in range(1, max(sides) + 1):
        if(sides[0] + sides[1] > max(sides) + i):
            newL.append(max(sides) + i)
    
    return len(newL)