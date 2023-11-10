import math
import sys
input = sys.stdin.readline

A = list(input().rstrip())

middle_pt = math.floor(len(A)/2)
# start는 입력한 인덱스값을 포함해서 그대로 나온다.
# end는 입력한 인덱스 -1까지 나온다.

if len(A) % 2 == 0:
    # 인덱스 2번까지
    reverse_A = A[::-1]
    if A[:middle_pt] == reverse_A[:middle_pt]:
        print(1)
    else:
        print(0)
else:
    reverse_A = A[::-1]
    if A[:middle_pt] == reverse_A[:middle_pt]:
        print(1)
    else:
        print(0) 