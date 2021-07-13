#https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    loc = month.index(a)
    sum_days = b
    
    for i in range(a-1):
        sum_days += days[i]

    answer = day[sum_days % 7]
    return answer
