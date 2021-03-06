#https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    
    if hand == "right":
        h = "R"
    else:
        h = "L"

    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11

    r = 12
    l = 10
    for j in range(len(numbers)):
        if numbers[j] in [1,4,7]:
            answer += "L"
            l = numbers[j]
        elif numbers[j] in [3,6,9]:
            answer += "R"
            r = numbers[j]
        elif numbers[j] in [2,5,8,11]:
            r1 = abs(r-numbers[j])//3 + abs(r-numbers[j])%3
            l1= abs(l-numbers[j])//3 + abs(l-numbers[j])%3
            if r1 == l1:
                answer += h
                if h == "R":
                    r = numbers[j]
                else:
                    l = numbers[j]
            elif r1 < l1:
                answer += "R"
                r = numbers[j]
            elif r1 > l1:
                answer += "L"
                l = numbers[j]
    return answer
