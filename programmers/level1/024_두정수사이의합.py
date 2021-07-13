#https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    x = min(a,b)
    y = max(a,b)
    
    for i in range(x,y+1):
        answer += i
   
    return answer
