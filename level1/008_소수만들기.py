#https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations as co

def solution(nums):
    a = list(co(nums,3))
    
    sum_a = []
    for i in range(len(a)):
        sum_a.append(sum(a[i]))

    li_last = []
    for i in sum_a:
        n = 0
        for j in range(1,i+1):
            if i % j == 0:
                n += 1
        if n == 2:
            li_last.append(i)

    answer = len(li_last)
   
    return answer
