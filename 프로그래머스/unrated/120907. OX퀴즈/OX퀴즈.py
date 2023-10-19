def solution(quiz):
    newL = []
    oxL = []
    for i in range(0, len(quiz)):
        newL.append(quiz[i].split("="))

    for i in newL:
        if(eval((i[0].split("="))[0]) == int(i[1])):
            oxL.append("O")
        else:
            oxL.append("X")
    return oxL