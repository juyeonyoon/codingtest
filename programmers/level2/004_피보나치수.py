#https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):

    num = 0
    a0 = 0
    a1 = 1
    if n == 1 and n == 2:
        a2 = 1
    else:
        while num < (n-1):
            num += 1
            a2 = a0 + a1
            a0 = a1
            a1 = a2

    answer = a2 % 1234567

    return answer
