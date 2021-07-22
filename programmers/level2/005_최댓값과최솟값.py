#https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    split_s = s.split(' ')
    li_s = []
    
    for i in split_s:
        li_s.append(int(i))

    answer = str(min(li_s)) + ' ' + str(max(li_s))
    return answer
