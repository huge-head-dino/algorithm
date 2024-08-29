def solution(my_string):
    answer = []
    temp = list(my_string)
    for i in range(len(my_string)):
        target = temp[i:len(my_string)+1]
        str_target = ''.join(target)
        answer.append(str_target)
    answer = sorted(answer)
    return answer