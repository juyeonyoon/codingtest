#https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations as cb

def solution(numbers):
    answer = []
    
    for i in list(cb(numbers,2)):
        answer.append(sum(i))   
    
    answer = sorted(list(set(answer)))
    return answer
