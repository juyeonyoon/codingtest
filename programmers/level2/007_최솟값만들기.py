#https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B): 
    A = sorted(A)
    B = sorted(B,reverse = True)
    answer = sum([a*b for a,b in zip(A,B)])
    return answer
