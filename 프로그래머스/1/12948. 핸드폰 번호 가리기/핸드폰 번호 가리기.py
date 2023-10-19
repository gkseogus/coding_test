def solution(phone_number):
    newL = []
    
    for i in range(0, len(phone_number[:-4])):
        newL.append("*")
        
    newL.append(phone_number[-4:])
    
    return ''.join(newL)