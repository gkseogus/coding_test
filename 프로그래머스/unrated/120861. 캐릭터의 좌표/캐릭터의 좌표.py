def solution(keyinput, board):
    zeroL = [0,0]   
    boardX = board[0]//2
    boardY = board[1]//2
    
    for i in keyinput:
        if(i == "up"):
            if(zeroL[1] >= boardY):
                zeroL[1] = boardY
            else:
                zeroL[1] += 1
        elif(i == "down"):
            if(zeroL[1] <= -boardY):
                zeroL[1] = -boardY
            else:
                zeroL[1] -= 1
        elif(i == "left"):
            if(zeroL[0] <= -boardX):
                zeroL[0] = -boardX
            else:
                zeroL[0] -= 1
        elif(i == "right"):
            if(zeroL[0] >= boardX):
                zeroL[0] = boardX
            else:
                zeroL[0] += 1
    
    return zeroL