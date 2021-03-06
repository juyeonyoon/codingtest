#https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    
    answer = []
    n = {}
    l = len(stages)

    for i in range(1,N+1):
        if l == 0:
            n[i] = 0
        else:
            n[i] = stages.count(i)/l
            l -= stages.count(i)

    n_desc = sorted(n.items(),key = lambda x: x[1],reverse = True)

    for i in range(len(n_desc)):
        answer.append(n_desc[i][0])
        
    return answer
