import sys
input = sys.stdin.readline
from collections import deque 


S = input().rstrip()
Boom = input().rstrip()

stack = []
Boom_len = len(Boom)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-Boom_len:]) == Boom:
        for _ in range(Boom_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")