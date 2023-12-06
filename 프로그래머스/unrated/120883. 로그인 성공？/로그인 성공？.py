def solution(id_pw, db):
    id_s = id_pw[0]
    pw_s = id_pw[1]
    
    loginMsg = []
    
    for i in db:
        if(i[0] == id_s and i[1] == pw_s):
            loginMsg.append("login")
        elif(i[0] == id_s and i[1] != pw_s):
            loginMsg.append("wrong pw")
        else:
            loginMsg.append("fail")
            
    if("login" in loginMsg):
        return "login"
    elif("wrong pw" in loginMsg):
        return "wrong pw"
    else:
        return "fail"