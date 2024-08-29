def solution(str_list, ex):
    temp = str_list.copy()
    for i,val in enumerate(str_list):
        if ex in val:
            temp.remove(val)
    answer = ''.join(temp)
    return answer