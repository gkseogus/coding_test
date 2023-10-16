def solution(todo_list, finished):
    newList = []
    dicList = { x:y for x,y in zip(todo_list, finished) }
    for key, value in dicList.items():
        if(value == False):
            newList.append(key)
    return newList
