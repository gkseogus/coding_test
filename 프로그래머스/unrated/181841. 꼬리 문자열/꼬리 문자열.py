def solution(str_list, ex):
    newStr = ""
    for i in str_list:
        if(ex not in i):
            newStr += i
    return newStr