def solution(x, n):
    answer = []
    res = x
    answer.append(x)
    for i in range(n-1):
        res += x
        answer.append(res)
    return answer