def solution(my_string, index_list):
    mys = ''
    for i in index_list:
        mys += my_string[i]
    return mys
