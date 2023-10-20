import math

def solution(s):
    return s[math.floor(len(s) / 2) - 1] + s[math.floor(len(s) / 2)] if(len(s) % 2 == 0) else s[math.floor(len(s) / 2)]
