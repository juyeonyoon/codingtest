#https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    num = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            num.append(absolutes[i])
        else:
            num.append(-absolutes[i])
    answer = sum(num)
    return answer
