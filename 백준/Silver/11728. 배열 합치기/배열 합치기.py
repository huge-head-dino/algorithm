import sys
input = sys.stdin.readline

A_num, B_num = map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

add = A + B
res = sorted(add)

print(*res, sep=' ')