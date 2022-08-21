#https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += i
        else:
            num = ord(i)
            if num <= 90:
                num += n
                if num > 90:
                    answer += chr(64+num%90)
                else:
                    answer += chr(num)
            elif num >= 97:
                num += n
                if num > 122:
                    answer += chr(96+num%122)
                else:
                    answer += chr(num)
    return answer
