import sys
input = sys.stdin.readline

N = int(input())
res = 1

for i in range(1,N+1):
    res = i * res

A = list(str(res))
A.reverse()

count = 0

for i in A:
    if i == '0':
        count += 1
    else: 
        break

print(count)

