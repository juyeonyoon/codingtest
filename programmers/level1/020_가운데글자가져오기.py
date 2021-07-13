#https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    l = len(s)//2
    if len(s) % 2 == 1:
        answer = s[l]
    else:
        answer = s[l-1:l+1]
    return answer
