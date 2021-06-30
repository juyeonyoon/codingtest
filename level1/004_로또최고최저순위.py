#https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    match = []
    num_0 = 0   
    for l in lottos:
        if l == 0:
            num_0 += 1
    for i in lottos:
        for j in win_nums:
            if i == j:
                match.append(i)
    for k in [len(match) + num_0, len(match)]:
        if k >= 2:
            answer.append(7-k)
        else:
            answer.append(6)
    return answer
