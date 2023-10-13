def solution(my_strings, parts):
    answer = ''
    
    for index, value in enumerate(parts):
        answer += my_strings[index][value[0]:value[1]+1]
    
    return answer