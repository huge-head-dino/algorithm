def solution(numbers, k):
    answer = 0
    a = len(numbers)
    b = 2 * (k-1)
    idx = b % a
    answer = numbers[idx]
    
    return answer