def solution(my_string, n):
    answer = ''
    my_string = my_string[::-1]
    my_string = my_string[:n]
    my_string = my_string[::-1]
    my_string = str(my_string)
    return my_string