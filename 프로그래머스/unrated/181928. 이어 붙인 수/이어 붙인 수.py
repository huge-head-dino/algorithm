def solution(num_list):
    answer = 0
    h = ''
    j = ''
    for i in num_list:
        if i % 2 == 0:
            a = str(i)
            h += a
        else:
            b = str(i)
            j += b
    h = int(h)
    j = int(j)   
    answer = h + j
    return answer