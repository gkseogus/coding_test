def solution(a, d, included):
    return sum(a + (index * d) for index, value in enumerate(included) if value)