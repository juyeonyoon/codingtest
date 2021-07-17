#https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    
    li_s = s.split(' ')
    
    for i in li_s:
        i_upper = i.capitalize()
        if answer == '':
            answer = i_upper
        else:
            answer = answer + ' ' + i_upper
            
    return answer
