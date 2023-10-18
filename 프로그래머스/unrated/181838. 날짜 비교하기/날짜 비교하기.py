def solution(date1, date2):
    dat1 = ''.join(map(str, date1))
    dat2 = ''.join(map(str, date2))
    if(int(dat1) < int(dat2)):
        return 1
    else:
        return 0
