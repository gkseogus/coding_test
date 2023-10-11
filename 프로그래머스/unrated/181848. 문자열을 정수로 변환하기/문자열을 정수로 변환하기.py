def solution(n_str):
    strN = []
    for i in n_str:
        if (i == "0"):
            strN.append(0)
        elif (i == "1"):
            strN.append(1)
        elif (i == "2"):
            strN.append(2)
        elif (i == "3"):
            strN.append(3)
        elif (i == "4"):
            strN.append(4)
        elif (i == "5"):
            strN.append(5)
        elif (i == "6"):
            strN.append(6)
        elif (i == "7"):
            strN.append(7)
        elif (i == "8"):
            strN.append(8)
        else:
            strN.append(9)
    return int(''.join(map(str, strN)))