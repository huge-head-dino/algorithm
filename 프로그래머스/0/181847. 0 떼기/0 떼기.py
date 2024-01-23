def solution(n_str):
    answer = ''
    temp = n_str
    for i in n_str:
        if i == '0':
            temp = temp[1:]
        else:
            break
    answer = temp
    return answer