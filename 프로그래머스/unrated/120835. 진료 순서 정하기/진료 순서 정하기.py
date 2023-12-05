def solution(emergency):
    newL = []
    tmp = sorted(emergency, reverse=True)

    for i in emergency:
        newL.append(tmp.index(i) + 1)
    
    return newL
