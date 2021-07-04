#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    
    result = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0
                break
    
    re = result
    while True:
        a = 0
        n = 1
        k = 0
        double = []
        for i in range(len(result)):
            if result[i] != a:
                double.append(result[i])
            else:
                double.pop(i-n)
                n += 2
                k += 1
            a = result[i]
        result = double
        if k == 0:
            break

    answer = len(re)-len(result)

    return answer
