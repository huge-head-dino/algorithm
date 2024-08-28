def solution(my_strings, parts):
    answer = ''
    my_strings = list(my_strings)
    for i,val in enumerate(parts):
        val = my_strings[i][val[0]:val[1]+1]
        answer += val
    return answer