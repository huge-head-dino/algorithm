import sys
input = sys.stdin.readline


N, M = map(int,input().split())
num = list(map(int, input().split()))
res = 0

for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            sum = num[a] + num[b] + num[c]
            if sum <= M:
                res = max( res , sum )
            else:
                continue

print(res)