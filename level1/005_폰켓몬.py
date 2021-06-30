#https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    unique = len(set(nums))
    if unique < len(nums)/2:
        answer = unique
    else:
        answer = int(len(nums)/2)
    return answer
