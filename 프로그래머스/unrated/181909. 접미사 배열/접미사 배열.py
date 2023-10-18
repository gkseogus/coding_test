def solution(my_string):
    for idx, val in reversed(list(enumerate(my_string))):
        print(my_string.endswith(my_string[idx]), my_string[idx])