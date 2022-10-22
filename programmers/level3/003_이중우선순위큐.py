#https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    li = []
    for i in range(len(operations)):
        if operations[i][0] == "I":
            li.append(operations[i][2:])
        elif operations[i] == "D 1":
            if li == []:
                li = []
            else:
                max_li = max([int(a) for a in li])
                li.remove(str(max_li))
        else:
            if li == []:
                li = []
            else:
                min_li = min([int(a) for a in li])
                li.remove(str(min_li))

    if li == []:
        answer = [0,0]
    else:
        max_an = max([int(a) for a in li])
        min_an = min([int(a) for a in li])
        answer = [max_an,min_an]

    return answer
