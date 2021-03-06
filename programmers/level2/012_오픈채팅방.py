#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    di_re = {}
    answer = []
    
    for i in record:
        sp_re = i.split(' ')
        if sp_re[0] == 'Enter' or sp_re[0] == 'Change':
            di_re[sp_re[1]] = sp_re[2]
            
    for i in record:
        sp_re = i.split(' ')
        if sp_re[0] == 'Enter':
            answer.append(di_re[sp_re[1]] + '님이 들어왔습니다.')
        elif sp_re[0] == 'Leave':
            answer.append(di_re[sp_re[1]] + '님이 나갔습니다.')
        else:
            continue
            
    return answer
