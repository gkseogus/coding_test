def solution(score):
    avg_list = []
    st_list = []
    
    # 평균 값 선정
    for i in score:
        avg_list.append((i[0] + i[1]) / 2.0)
    
    # 등수를 저장할 리스트 초기화
    rank = [1] * len(avg_list)
    
    # 등수 값 선정
    for i in range(len(avg_list)):
        for j in range(len(avg_list)):
            if avg_list[i] < avg_list[j]:
                rank[i] += 1
    
    if(len(score) == 1):
        return [1]
    
    st_list = rank
    return st_list