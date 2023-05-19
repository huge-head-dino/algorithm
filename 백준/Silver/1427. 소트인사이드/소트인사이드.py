import sys
input = sys.stdin.readline

N = list(str(int(input())))

N.sort()
N.reverse()

print(''.join(N))

