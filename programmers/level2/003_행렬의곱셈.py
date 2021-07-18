#https://programmers.co.kr/learn/courses/30/lessons/12949

#1st solution - numpy 활용

import numpy as np

def solution(arr1, arr2):
    an = np.dot(arr1,arr2)
    answer = an.tolist()
    return answer

#2nd solution - 모듈 사용 X, 행렬의 곱셈 원리 이용한 코드

def solution(arr1, arr2):
    answer = []
    new_arr2 = list(map(list,zip(*arr2)))
    
    for i in arr1:
        an = []
        for j in new_arr2:
            an.append(sum([x*y for x,y in zip(i,j)]))
        answer.append(an)
    
    return answer
