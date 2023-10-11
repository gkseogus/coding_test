def solution(num_list):
    even, odd = [], []
    
    for i in num_list:
        if(i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    return int("".join(map(str, even))) + int("".join(map(str, odd)))