#https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    li_s = sorted(s,reverse = True)
    for i in li_s:
        answer += i
    return answer
