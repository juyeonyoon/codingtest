#https://school.programmers.co.kr/learn/courses/30/lessons/49993

import re

def solution(skill, skill_trees):
    sub = "[^" + skill + "]"
    word_re = [re.sub(sub,"", word) for word in skill_trees] 
    
    li = []
    temp = ""
    for i in skill:
        temp += i 
        li.append(temp)
        
    answer = 0
    for i in word_re:
        if (i in li) or (i == ""):
            answer += 1
            
    return answer
