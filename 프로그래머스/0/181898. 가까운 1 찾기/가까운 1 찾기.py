def solution(arr, idx):
    answer = 0
    arr_c = arr[idx:]
    for i,val in enumerate(arr):
        if i >= idx:
            if 1 in arr_c:
                if val == 1:
                    answer = i
                    break
            else:
                answer = -1
    return answer