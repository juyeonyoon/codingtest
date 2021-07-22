#https://programmers.co.kr/learn/courses/30/lessons/12924

import math

def solution(n):
    answer = 0
    
    for k in range(int(math.sqrt(1+8*n)/2)):
        a = (2*n/(k+1)-k)/2
        if a.is_integer() and a > 0:
            answer += 1

    return answer


1. 시그마(Σ) 정의와 공식 이용

 a ~ a+k 더하는 공식 
 sum = {(2a+k)(k+1)}/2 a <=> a = (2*sum/(k+1)-k)/2


2. 문제 풀이에서 for문의 k 범위를 어떻게 설정하였는지에 대한 설명은 다음과 같다. 

문제에서 조건: a > 0, k > 0
a = (2*sum/(k+1)-k)/2 > 0 을 이용해 k의 범위 구하면, 0 < k < (-1 + sqrt(1+8*sum))/2 라는 것을 알 수 있다.
