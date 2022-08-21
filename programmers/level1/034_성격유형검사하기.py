#https://school.programmers.co.kr/learn/courses/30/lessons/118666

from collections import defaultdict

def solution(survey, choices):
    final_dic = defaultdict(int)

    for i in range(len(survey)):
        if choices[i] <= 3:
            final_dic[survey[i][0]] += (4 - choices[i])
        elif choices[i] >= 5:
            final_dic[survey[i][1]] += (choices[i] - 4)
        else:
            pass

    answer = ""
    ch_type = ["RT","CF","JM","AN"]
    for i in range(4):
        if final_dic[ch_type[i][0]] >= final_dic[ch_type[i][1]]:
            answer += ch_type[i][0]
        else:
            answer += ch_type[i][1]

    return answer
