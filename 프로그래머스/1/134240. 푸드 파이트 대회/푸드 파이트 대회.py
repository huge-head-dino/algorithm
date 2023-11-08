import math
def solution(food):
    answer = ''
    for idx, val in enumerate(food):
        if idx == 0:
            continue
        if val % 2 == 0:
            put_num = val
            push_idx = int(len(answer) / 2)
            answer = answer[:push_idx] + str(str(idx)*put_num) + answer[push_idx:]
        else:
            put_num = val-1
            push_idx = int(len(answer) / 2)
            answer = answer[:push_idx] + str(str(idx)*put_num) + answer[push_idx:]
    answer = answer[:int(len(answer)/2)] + '0' + answer[int(len(answer)/2):]
    return answer