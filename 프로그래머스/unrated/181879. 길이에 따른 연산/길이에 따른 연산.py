def solution(num_list):
    answer = 0
    res = 1
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        for i in num_list:
            res = res * i
            answer = res
    return answer