#https://programmers.co.kr/learn/courses/30/lessons/12909

<방법1> - 효율성 만족

def solution(s):
    num_l = s.count('(')
    num_r = s.count(')')
    l = 0
    r = 0

    if s[0] == ')' or s[-1] == '(':
        answer = False
    else:
        if num_l == num_r:
            for i in s:
                if i == '(':
                    l += 1
                else:
                    r += 1
                if l < r:
                    answer = False
                    break
                else:
                    answer = True
        else:
            answer = False
            
    return answer

num_l 은 문자열의 '(' 개수
num_r 은 문자열의 ')' 개수
l과 r 변수 역시 문자열의 '(',')' 개수 나타내지만, 총 개수를 의미하기보다는 for문 안에 사용함으로써 개수를 차례대로 계산(순간의 개수 의미)
r의 값[ ')' 개수] 이  l의 값['(' 개수] 보다 많아지는 순간 answer는 Flase

<방법2> - 효율성 불만족

def solution(s):
    while True:
        new_s = s.replace('()','',1)
        if new_s == s:
            break
        s = new_s 
    if s == '':
        answer = True
    else:
        answer = False
 
    return answer

while문으로 인해 시간 초과 
