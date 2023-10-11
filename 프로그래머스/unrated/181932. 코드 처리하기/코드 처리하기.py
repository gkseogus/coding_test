def solution(code):
    mode = 0
    ret = ""

    for index, value in enumerate(code):
        if mode == 0:
            if value == "1":
                mode = 1
            if value != "1" and index % 2 == 0:
                ret += value
        else:
            if value == "1":
                mode = 0
            if value != "1" and index % 2 != 0:
                ret += value
    if ret == "":
        return "EMPTY"
    return ret
