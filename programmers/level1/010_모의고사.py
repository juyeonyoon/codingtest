#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):

    answer = []
    st1 = [1,2,3,4,5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    l_st1 = []
    l_st2 = []
    l_st3 = []
    
    for i in range(len(answers)):
        k1 = ((i+1)%len(st1))-1
        k2 = ((i+1)%len(st2))-1
        k3 = ((i+1)%len(st3))-1
        if answers[i] == st1[k1]:
            l_st1.append(answers[i])
        if answers[i] == st2[k2]:
            l_st2.append(answers[i])
        if answers[i] == st3[k3]:
            l_st3.append(answers[i])

    l1 = len(l_st1)
    l2 = len(l_st2)
    l3 = len(l_st3)
    max_st = max(l1,l2,l3)
    
    if max_st == l1:
        answer.append(1)
    if max_st == l2:
        answer.append(2)
    if max_st == l3:
        answer.append(3)
    
    return answer
