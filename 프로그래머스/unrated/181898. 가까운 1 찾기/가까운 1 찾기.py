def solution(arr, idx):
    cnt = -1
    for ide, val in enumerate(arr):
        if(ide + 1 > idx and val == 1):
            return ide
    return -1