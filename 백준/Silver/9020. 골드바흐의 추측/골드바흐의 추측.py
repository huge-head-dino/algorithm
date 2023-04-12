import sys
T = int(sys.stdin.readline())

# 에라토스테네스의 체로 소수인 리스트 만들기
x = 10000
array = [True for i in range(x+1)]
for i in range(2, int(x**(0.5))+1):
    if array[i] == True:
        j = 2
        while i*j <= x:
            array[i*j] = False
            j += 1


# 맨처음엔 이 방식으로 했으나, 승규 행님이 효율성면에서 어차피 i에 0을 집어넣으면 똑같다.
# 따라서 실제로 사용된 코드로 돌리는 것이 효율적이다.라고 하셨음
# for _ in range(T):
#     n = int(sys.stdin.readline())
#     if array[n//2]:
#         print(int(n/2), int(n/2))
#     elif array[n//2] is False:
#         for i in range(n//2):
#             if array[n//2-i] and array[n//2+i]:
#                 print(int(n/2-i), int(n/2+i))
#                 break

for _ in range(T):
    n = int(sys.stdin.readline())
    for i in range(n//2):
        if array[n//2-i] and array[n//2+i]:
            print(int(n/2-i), int(n/2+i))
            break