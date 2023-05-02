import sys
input =sys.stdin.readline

N, K = map(int,input().split())

coins = []
for _ in range(N):
    a = int(input())
    coins.append(a)

coins.reverse()
count = 0

for coin in coins:
    if K // coin == 0:
        continue
    elif K // coin >= 1:
        candidate = K // coin
        K = K % coin
        count += candidate

print(count)



