def solution(my_string, is_suffix):
    answer = 0
    my_leng = len(my_string)
    is_leng = len(is_suffix)
    my_string = my_string[::-1]
    my_string = my_string[:len(is_suffix)]
    my_string = my_string[::-1]
    
    if my_leng < is_leng:
        return 0
    if my_string == is_suffix:
        return 1
    else:
        return 0 