def solution(rsp):
    newL = []
    
    for i in rsp:
        if(i == "2"):
            newL.append("0")
        elif(i == "0"):
            newL.append("5")
        else:
            newL.append("2")
    
    return "".join(newL)