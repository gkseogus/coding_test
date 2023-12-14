def solution(strArr):
    tmp = []
    answer = [len(i) for i in strArr]

    for i in set(answer):
        tmp.append(answer.count(i))
    
    return max(tmp)
