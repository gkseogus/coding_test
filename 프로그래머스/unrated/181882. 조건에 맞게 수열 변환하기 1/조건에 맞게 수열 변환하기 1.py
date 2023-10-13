def solution(arr):
    return [int(i / 2) if i >= 50 and i % 2 == 0 else i * 2 if i < 50 and i % 2 != 0 else i for i in arr]