#https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True
        else:
            answer = False
    else: 
        answer = False
    return answer
