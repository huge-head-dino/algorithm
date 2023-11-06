def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    cursor = 10000000
    for i in arr:
        if i < cursor:
            cursor = i
    arr.remove(cursor)
    return arr