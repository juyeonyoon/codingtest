#https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    
    num = 0
    if w == 1 or h == 1:
        answer = 0
    elif w == h:
        answer = w*h-w
    else:
        for i in range(1, w):
            h_len = h*i/w
            num += int(h_len)
        answer = num*2  
    
    return answer
