def solution(strArr):
    return [i.lower() if(int(strArr.index(i)) % 2 == 0) else i.upper() for i in strArr] 