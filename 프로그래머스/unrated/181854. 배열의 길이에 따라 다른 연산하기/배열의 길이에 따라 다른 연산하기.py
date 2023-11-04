def solution(arr, n):
    if len(arr) % 2 == 1:
        for idx , value in enumerate(arr):
            if idx % 2 == 0:
                arr[idx] += n
    
    elif len(arr) % 2 == 0:
        for idx , value in enumerate(arr):
            if idx % 2 == 1:
                arr[idx] += n        
    return arr