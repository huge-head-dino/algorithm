import sys
input = sys.stdin.readline

N = list(str(int(input())))

N.sort()
N.reverse()

#프린트방식
print(''.join(N))

