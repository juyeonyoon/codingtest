#https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i])/speeds[i])
        days.append(day)
    answer = []
    a = 0
    for j in days:
        if a < j:
            n = 1
            answer.append(n)
            a = j
        else:
            answer[-1] += 1
    return answer
