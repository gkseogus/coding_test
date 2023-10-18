def solution(myString, pat):
    newString = ''
    for i in myString:
        if(i == 'A'):
            newString += 'B'
        else:
            newString += 'A'
    return 1 if(pat in newString) else 0