def solution(my_string):
    newL = []
    for i in range(len(my_string)):
        newL.append(my_string[i:])
    return sorted(newL)