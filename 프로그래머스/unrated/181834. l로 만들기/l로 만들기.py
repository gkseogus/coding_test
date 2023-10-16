def solution(myString):
    arr = ['a','b','c','d','e','f','g','h','i','j','k']
    for idx, val in enumerate(myString):
        if(val in arr):
            myString = myString[:idx] + 'l' + myString[idx+1:]
    return myString

