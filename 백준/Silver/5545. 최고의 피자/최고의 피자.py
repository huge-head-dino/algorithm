import sys
import math

input = sys.stdin.readline

N = int(input())
PR_D, PR_T = map(int,input().split())
dough = int(input())
toppings = []
res=0


for i in range(N):
    topping = int(input())
    toppings.append(topping)
# 내림차순으로 만들어줘야만 아래 슬라이스가 성립
# 1개만 고른놈중엔 index[0]이 젤 효율적
# 2개만 고른놈중엔 index[0]하고 [1]이 젤 효율적
jung = sorted(toppings, reverse=True)

# range(N+1)이 아니라 len(jung)+1인 이유:


for i in range(N+1):
    price = PR_D + PR_T * (i)
    res = max(res, (dough+sum(jung[:i]))//price)


print(res)
