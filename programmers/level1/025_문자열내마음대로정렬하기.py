#https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    d = {}

    for i in strings:
        d[i] = i[n]

    d = sorted(d.items(),key = lambda x: (x[1], x[0]))

    for k,v in d:
        answer.append(k)

    return answer
