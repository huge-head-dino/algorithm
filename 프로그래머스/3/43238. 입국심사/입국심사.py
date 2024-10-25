def solution(n, times):
    left , right = 1 , max(times) * n
    
    while left <= right:
        mid = (left+right)// 2
        target = 0
        for time in times:
            target += mid // time
            if target >= n:
                break
        if target < n:
            left = mid + 1
        else:
            right = mid - 1
    return left