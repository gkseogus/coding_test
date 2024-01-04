def solution(arr, flag):
    newL = []
    
    for i in range(len(flag)):
        if(flag[i] == True):
            for j in range(0, arr[i] * 2):
                newL.append(arr[i])
        else:
            for k in range(1, arr[i] + 1):
                newL.pop()
    return newL