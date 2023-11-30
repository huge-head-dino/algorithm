from collections import deque 
def solution(arr):
    answer = 0
    n = 0
    arr_new = deque(arr)
    for i in range(2,len(arr)+1):
        n = 0
        a = arr_new.popleft()
        b = arr_new.popleft()
        while True:
            n += 1
            if n % a == 0 and n % b ==0:
                arr_new.appendleft(n)
                break
    return arr_new[0]