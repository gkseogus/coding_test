def solution(my_string):
    numL = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    newL = []
    
    for i in my_string:
        if(i in numL):
            newL.append(int(i))
    
    return sorted(newL)