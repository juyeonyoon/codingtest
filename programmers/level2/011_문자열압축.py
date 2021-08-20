#https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    
    #다음 함수는 n개 단위로 압축했을 때의 단어의 길이를 나타낸다. 
    def num(n):
        li = []
        for i in range(0,len(s),n):
            li.append(s[i:i+n]) 
        li.append(0)
        an = []
        k = 1
        for i in range(len(li)-1):
            if li[i] != li[i+1]:
                an.append(li[i])
                k = 1
            else:
                k += 1
                an = list(an)
                an.append(k)
                if k > 2:
                    an.pop(len(an)-2)

        an = ''.join(map(str,an))
        return len(an)   

    if len(s) != 1:
        li_n = list(i for i in range(1,int(len(s)/2)+1))
    else:
        li_n = [1]
        
    li_num = []
    for i in li_n:
        li_num.append(num(i))

    answer = min(li_num)

    return answer
