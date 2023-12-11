def solution(myStr):
    repL = myStr.replace("a", "-").replace("b", "-").replace("c", "-").split("-")
    newL = [i for i in repL if i]
    
    if(len(newL) == 0):
        return ["EMPTY"]
    return newL