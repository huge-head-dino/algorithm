import sys
input = sys.stdin.readline
from collections import deque
N = int(input())

card_queue = deque()

for i in range(N):
    card_queue.append(i+1)

while len(card_queue)>1:
    card_queue.popleft()
    card_queue.append(card_queue.popleft())

print(card_queue.pop())