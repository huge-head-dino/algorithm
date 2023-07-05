import sys
input = sys.stdin.readline

N = int(input())
S = input()
result = 0

for i in range(N):
    num = int(S[i])
    result += num


print(result)