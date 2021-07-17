#https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):

    multi= 1
    for i in arr:
        multi *= i

    for i in range(max(arr),multi+1, max(arr)):
        num = 0
        for j in arr:
            if i % j == 0:
                num += 1
        if num == len(arr):
            answer = i
            break
        
    return answer
