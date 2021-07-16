#https://programmers.co.kr/learn/courses/30/lessons/12921

<에라토스테네스의 체 이용한 알고리즘>
#https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

def solution(n):
    li_num = [1 for i in range(n+1)]
    for i in range(2,n+1):
        if li_num[i] == 1:
            a = 2
            while i*a <= n:
                li_num[i*a] = 0
                a += 1
    answer = sum(li_num)-2
    return answer
