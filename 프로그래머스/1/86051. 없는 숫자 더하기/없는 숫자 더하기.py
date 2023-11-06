def solution(numbers):
    answer = 0
    arr = [0,1,2,3,4,5,6,7,8,9]
    numbers = sorted(numbers)
    
    for i in numbers:
        if i in arr:
            arr.remove(i)
    answer = sum(arr)
    return answer