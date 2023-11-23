def solution(num_list):
    answer = -1
    for idx, val in enumerate(num_list):
        if val < 0:
            return idx
    else:
        return answer