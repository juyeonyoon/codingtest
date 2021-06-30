#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    par = sorted(participant)
    com = sorted(completion)
    for i in range(len(com)):
        if par[i] == com[i]:
            answer = par[i+1]
        elif par[i] != com[i]:
            answer = par[i]
            break
    return answer
