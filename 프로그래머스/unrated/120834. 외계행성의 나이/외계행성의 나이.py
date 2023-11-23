def solution(age):
    answer = ''
    ageCode = ["a", "b", "c", "d", "e", "f","g","h","i","j"]
    
    for i in str(age):
        answer += ageCode[int(i)]
        
    return answer