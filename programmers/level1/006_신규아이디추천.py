#https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    
    id1 = new_id.lower()
    id2 = re.sub("[^a-z0-9-_.]","",id1)
    id3 = re.sub("\.+",".",id2)
    
    id4 = id3
    if id4 == "":
        id4 ="a"
    elif id4[0] == '.':
        id4 = id4[1:]
    if id4 == "":
        id4 = "a"
    elif id4[len(id4)-1] == '.':
        id4 = id4[0:len(id4)-1]


    id5 = id4
    if len(id5) >= 16:
        id6 = id5[:15]
    else:
        id6 = id5  
    if id6[len(id6)-1] == '.':
        id6 = id6[:len(id6)-1]

    if len(id6) <= 2:
        id7 = id6 + id6[len(id6)-1]*(3-len(id6))
    else:
        id7 = id6
    
    return id7
