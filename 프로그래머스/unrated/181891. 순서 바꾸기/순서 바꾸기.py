def solution(num_list, n):
    answer = []
    slice_list = num_list[n:]
    num_list = num_list[:n]
    slice_list += num_list
    return slice_list