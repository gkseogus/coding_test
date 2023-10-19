def solution(absolutes, signs):
    dictL = dict(zip(absolutes, signs))
    sumC = []
    
    for abs, sig in zip(absolutes, signs):
        if(sig == True):
            sumC.append(abs)
        else:
            sumC.append(-abs)
    
    return sum(sumC)