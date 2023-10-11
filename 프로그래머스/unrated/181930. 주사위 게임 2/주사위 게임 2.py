def solution(a, b, c):
    if (a != b and a != c and b != c):
        return (a + b + c)
    elif (a == b == c):
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    if (a == b):
        if((a and b) != c):
            return (a + b + c) * (a**2 + b**2 + c**2)
    if (b == c):
        if((b and c) != a):
            return (a + b + c) * (a**2 + b**2 + c**2)
    if (a == c):
          if((a and c) != b):
            return (a + b + c) * (a**2 + b**2 + c**2)  