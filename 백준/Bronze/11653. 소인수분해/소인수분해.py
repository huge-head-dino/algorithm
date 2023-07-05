import sys
input = sys.stdin.readline

N = int(input())
result = []

# 2부터 N까지
i = 2
while(i <= N):
    while(N % i == 0):
            result.append(i)
            N = N / i
    i += 1

for i in result:
 print(i)