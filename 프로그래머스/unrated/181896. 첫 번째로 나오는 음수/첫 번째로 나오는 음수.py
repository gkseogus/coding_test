def solution(num_list):
    listLen = []
    for i in num_list:
        if(i < 0):
            return num_list.index(i)
        else:
            listLen.append(i)
    if(len(listLen) == len(num_list)):
            return -1