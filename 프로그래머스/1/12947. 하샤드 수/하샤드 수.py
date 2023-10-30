def solution(x):
    answer = True

    res = list(map(int, str(x)))
    sum_res = sum(res)
    if x % sum_res == 0:
        answer = True
    else:
        answer = False
    return answer