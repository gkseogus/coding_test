def solution(my_string, overwrite_string, s):
    overwrite_length = len(overwrite_string)
    new_string = my_string[:s] + overwrite_string + my_string[s + overwrite_length:]
    return new_string