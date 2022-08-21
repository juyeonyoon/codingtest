#https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    q_li=[]

    if n > s:
        q_li = [-1]
    else:
        q = s // n 
        r = s % n
        q_li = [q]*n
        
        for i in range(r):
            q_li[i] += 1
            
        q_li.sort()
        
    answer = q_li
    return answer
