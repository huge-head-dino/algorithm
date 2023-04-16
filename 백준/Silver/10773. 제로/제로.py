import sys
input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
    T = int(input())
    if T == 0:
        stack.pop()
    else:
        stack.append(T)


print(sum(stack))