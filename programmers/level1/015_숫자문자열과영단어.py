#https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num = ['0','1','2','3','4','5','6','7','8','9']
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''

    while s != '':
        for i in range(len(num)):
            if s == '':
                answer = answer
            elif s[0] == num[i]:
                answer = answer + num[i]
                s = s.replace(num[i],"",1)
            elif s.find(word[i]) == 0:
                answer = answer + num[i]
                s = s.replace(word[i],"",1)
            else:
                answer = answer 

    answer = int(answer)
    return answer
