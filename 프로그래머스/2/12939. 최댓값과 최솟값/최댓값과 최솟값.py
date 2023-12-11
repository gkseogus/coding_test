def solution(s):
    newL = list(map(int, s.split()))
    
    return str(min(newL)) + ' ' + str(max(newL))