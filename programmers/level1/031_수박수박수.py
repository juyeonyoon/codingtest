#https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = '수박'
    if n % 2 == 0:
        answer = answer*(n//2)
    else:
        answer = answer*(n//2)+'수'
    return answer
