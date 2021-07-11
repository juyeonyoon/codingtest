#https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    
    reverse = ''
    while True:
        reverse += str(n % 3)
        n = n // 3
        if n == 0:
            break

    exp = 0
    answer = 0
    for i in reverse[::-1]:
        answer += int(i)*(3**exp)
        exp += 1
            
    return answer
