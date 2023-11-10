import sys
input = sys.stdin.readline

A = list(input().rstrip())

# 26개
alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for idx, val in enumerate(alpha):
    if val in A:
        res = A.index(val)
        alpha[idx]=res
    else:
        alpha[idx]= -1

print(*alpha)