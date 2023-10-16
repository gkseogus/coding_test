def solution(arr, n): 
    if(len(arr) % 2 != 0):
        return [ val + n if(idx % 2 == 0) else val for idx,val in enumerate(arr)]
    if(len(arr) % 2 == 0):
        return [ val + n if(idx % 2 != 0) else val for idx,val in enumerate(arr)]
        
