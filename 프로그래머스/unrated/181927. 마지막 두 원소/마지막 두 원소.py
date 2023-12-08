def solution(num_list):
    answer = []
    a = num_list.pop()
    b = num_list.pop()
    if a > b:
        num_list.append(b)
        num_list.append(a)
        num_list.append(a-b)
    else:
        num_list.append(b)
        num_list.append(a)
        num_list.append(a*2)
    return num_list