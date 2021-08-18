#https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    arr_num_n = '0'
    a = 1
    num = [10,11,12,13,14,15]
    word = ['A','B','C','D','E','F']

    while True:
        copy_a = a
        num_n = ''

        while copy_a > 0:
            remainder = copy_a % n
            if remainder in num:
                remainder = word[remainder-10]
            num_n += str(remainder)
            copy_a = copy_a // n

        num_n = num_n[::-1]
        # n진수 구하는 알고리즘 

        arr_num_n += num_n
        a += 1
        if len(arr_num_n) >= m*(t-1)+p:
            break                           
        
        #while문 반복을 최소화 하기 위해 arr_num_n 배열의 길이를 제한하였다. 

    for i in range(t):
        answer += arr_num_n[m*i+(p-1)]
            
    return answer
