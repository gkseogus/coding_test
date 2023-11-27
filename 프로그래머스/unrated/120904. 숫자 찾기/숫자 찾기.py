def solution(num, k):
    for idk, val in enumerate(str(num)):
        if(int(val) == k):
            return idk + 1

    return -1