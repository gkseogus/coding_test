import math

def solution(numer1, denom1, numer2, denom2):
    newL = [0, 0]
    newL[0] = numer1 * denom2 + numer2 * denom1
    newL[1] = denom1 * denom2
    
    
    gcd_value = math.gcd(newL[0], newL[1])

    newL[0] = newL[0] / gcd_value
    newL[1] = newL[1] / gcd_value
    
    return newL