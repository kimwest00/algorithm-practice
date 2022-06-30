#k번 이상 신고된 유저는 정지되며
#해당 유저를 신고한 유저의 정지 소식을 메일로 발송해준다
#매개변수 입력값
#1. 전체 유저 ID (id_list)
#2. 해당 유저가 신고한 ID(report)
    #report의 원소는 "이용자 ID 신고한 ID"형태로 담겨져있다
    #같은 유저가 이용자를 여러번 신고한 경우 1회신고라고 가정함
#3. 정지 기준 횟수 (k)
#출력값
    #각 유저가 메일을 받은 횟수를 리스트에 담아서 반환하시오
    #자기가 신고한 사람이 정지받으면 +1
    #자기가 정지당하면 +1
    #만약에 정지당했는데 그 이후에 신고하면?<-신고한 모든내용을 취합하고 마지막으로
    #이용정지를 시키며 정지메일을 발송하므로 안되겠다!
    
def solution(id_list, report, k):
    #report 리스트 중복제거
    #A->B A->B가 여러번 등장해도 어차피 1회로 치니까!
    n = len(id_list)
    
    mail = [[] for _ in range(n)]
    report = list(set(report))
    for index,key in enumerate(report):
        key = key.split()
        #id_list에서 신고받은사람의 index를 찾아낸다
        warn_index = id_list.index(key[-1])
        mail[warn_index].append(key[0])
        
    answer = [0 for _ in range(n)]
    for index, warn_list in enumerate(mail):
        if len(warn_list) >= k:
            for i in warn_list:
                answer[id_list.index(i)] += 1
    return answer