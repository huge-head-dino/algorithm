import sys
input = sys.stdin.readline

N = int(input())

for i in range(1,N+1):
    S = i + sum(list(map(int,str(i))))
    if (S == N):
        print(i)
        break
else:
    print(0)
        