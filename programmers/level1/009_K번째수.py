#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        split = sorted(array[i-1:j])
        answer.append(split[k-1])
    return answer
