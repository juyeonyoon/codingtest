#https://programmers.co.kr/learn/courses/30/lessons/12899

import math

def solution(n):
    
    answer = ''
    li_124 = [4,1,2,4]
    order = math.ceil(math.log(2*n/3+1,3))       # 3^a: a 값이 1부터 n일때까지의 합 = 3*(3^a-1)/2 이 식을 이용해 a 기준으로 식을 변환 
    order_part = int(n - 3*(3**(order-1)-1)/2)   # 중복순열 쭉 나열 했을 때 나열 횟수를 몇번해야되는지 알아보기 위한 식 -> n에서 그 전 나열 순서까지 빼준다. 
    order = order-1
    
    division = 0
    remainder = n
    
    #이어서 붙이는 방법
    while order > 0:                               
        division = math.ceil(order_part/(3**order))  
        remainder = order_part % (3**order)
        answer += str(li_124[division])
        order -= 1
        order_part = remainder

    answer = answer + str(li_124[remainder])  #while문에는 마지막 값이 입력되지 않는다. 마지막 값 입력
        
    return answer


#동일한 문제의 알고리즘 - n값이 엄청 커질 경우 시간초과로 에러가 날 수 있다. 

from itertools import product as pr
import math

def solution(n):
    
    order = math.ceil(math.log(2*n/3+1,3)) 
    order_part = int(n - 3*(3**(order-1)-1)/2)     
    
    li_124 = [1,2,4]
    li_n_order = list(pr(li_124, repeat=order))
    an = li_n_order[order_part-1]
    
    answer = ''
    for i in an:
        answer += str(i)
        
    return answer
