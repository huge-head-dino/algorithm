import sys
from collections import deque 
input = sys.stdin.readline


S = input().rstrip()

M = int(input())

order_left = deque(S)
order_right = deque()

for _ in range(M):
    A = input().rstrip()
    if A[0] == 'L':
        if not order_left:
            continue
        Lpop = order_left.pop()
        order_right.appendleft(Lpop)
    elif A[0] == 'D':
        if not order_right:
            continue
        Dleftpop = order_right.popleft()
        order_left.append(Dleftpop)
    elif A[0] == 'B':
        if not order_left:
            continue
        else:
            order_left.pop()
    elif A[0] == 'P':
        order_left.append(A[2])

res = order_left + order_right

print(''.join(res))