def solution(number):
    newL = []
    for i in map(int, str(number)):
        newL.append(i)
    return sum(newL) % 9
        