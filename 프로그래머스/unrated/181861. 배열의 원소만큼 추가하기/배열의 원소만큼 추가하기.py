def solution(arr):
    newArr = []
    for i in arr:
        for j in range(1,i+1):
            newArr.append(i)
    return newArr