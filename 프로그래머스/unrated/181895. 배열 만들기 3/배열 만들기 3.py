def solution(arr, intervals):
    val1, val2 = intervals[0]
    val3, val4 = intervals[1]
    
    return arr[val1:val2 + 1] + arr[val3: val4 + 1]