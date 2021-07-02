#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    
    for i in lost[:]:
        for j in reserve[:]:
            if i == j:
                lost.remove(i)
                reserve.remove(i)

    lost_num = []
    reserve_num = []
    
    for i in lost:
        lost_num.append(0)
    for j in reserve:
        reserve_num.append(2)
    
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if reserve[j]-1 == lost[i] and lost_num[i] == 0 and reserve_num[j] == 2:
                lost_num[i] += 1
                reserve_num[j] -= 1 
            elif reserve[j]+1 == lost[i] and lost_num[i] == 0 and reserve_num[j] == 2:
                lost_num[i] += 1
                reserve_num[j] -= 1

    num = 0
    for i in lost_num:
        if i == 0:
            num += 1

    answer = n - num
    
    return answer
