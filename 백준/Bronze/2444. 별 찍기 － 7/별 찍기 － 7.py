from collections import deque

import sys
input = sys.stdin.readline

# 가장 긴 별문자열을 만들어서 먼저 deque에 집어넣는다.
# 별 두개를 빼고 앞뒤로 공백을 두개붙인 문자열을 leftappend, append한다.
# 별의 값이 1보다 작아지면 그만 붙인다.

# deque에 들어있는 요소들을 for문으로 print한다.

A = int(input())
last_num = (A*2)-1

LCS = '*' * last_num

res = deque()
res.append(LCS)

for i in range(1,A):
    last_num = last_num-2
    MCS = ' '* i + '*' * (last_num)
    res.appendleft(MCS)
    res.append(MCS)

res = list(res)
res_one = res[:-1]
for i in res_one:
    print(i)
print(res[-1],end='') 