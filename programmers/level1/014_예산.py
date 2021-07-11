#https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    if sum(d) <= budget:
        answer = len(d)
    else:
        while True:
            budget -= min(d)
            if budget < 0:
                break
            d.remove(min(d))
            answer += 1
    return answer
