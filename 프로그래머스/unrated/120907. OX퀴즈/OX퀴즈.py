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
        #print(eval((i[0].split("="))[0]), i[1])
        #print(eval((quiz[0].split("="))[0]), (quiz[0].split("="))[1])
