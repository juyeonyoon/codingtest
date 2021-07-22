#https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    k = n  
    
    n_bi = ''   
    while True:
        n_bi += str(n % 2)
        n = n // 2
        if n == 0:
            break
            
    n_bi = n_bi[::-1]
    
    num_n1 = 0
    for i in n_bi:
        if i == '1':
            num_n1 += 1

    while True:
        k += 1
        a = k
        a_bi = ''
        while True:
            a_bi += str(a % 2)
            a  = a // 2
            if a == 0:
                break
                
        a_bi = a_bi[::-1]
        
        num_a1 = 0
        for i in a_bi:
            if i == '1':
                num_a1 += 1
        
        if num_a1 == num_n1:
            break
  
    answer = k
    return answer


<변수 이름 설명>

1. n_bi, a_bi : n, a의 이진법(binary system)
2. num_n1, num_a2 : n_bi, a_b1에서 1의 개수
