def solution(n, arr1, arr2):
    arr1B = []
    arr2B = []
    resultL = []
    
    for i in range(0, n):
        arr1B.append(bin(arr1[i]))
        arr2B.append(bin(arr2[i]))
        
    for j in range(len(arr1B)):
        result = (int(arr1B[j], 2) | int(arr2B[j], 2))
        if(len(''.join(bin(result).split("0b"))) < n):
            resultL.append((''.join(bin(result).split("0b")).replace("1", "#").zfill(n)).replace("0", ' '))
        else:
            resultL.append(''.join(bin(result).split("0b")).replace("1", "#").replace("0", ' '))
        
    return resultL