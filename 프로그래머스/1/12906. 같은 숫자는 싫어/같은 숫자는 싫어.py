from collections import deque
def solution(arr):
    left = []
    temp = arr.copy()
    right = deque(temp)
    
    for _ in arr:
        test = right.popleft()
        if not left:
            left.append(test)
            continue
        if left[-1] != test:
            left.append(test)
        else:
            pass
    return left