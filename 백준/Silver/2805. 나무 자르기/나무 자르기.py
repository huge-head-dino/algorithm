import sys
input = sys.stdin.readline

N, M = map(int,input().split())

tree = list(map(int, input().split())) #

start, end = 1, max(tree) #바닥부터 가장 높은 길이를 가진 나무까지 탐색범위를 걸겠다.

while start <= end: #가장 알맞는 H 길이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0 # M과 비교해야하는 이미 썰어버린 나무량
    for i in tree:
        if i >= mid:
            log += i - mid
    
    # H를 이분탐색으로 골라낸다.
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
