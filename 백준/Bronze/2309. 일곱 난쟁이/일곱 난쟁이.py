import sys
import itertools
input = sys.stdin.readline


num = [0,1,2,3,4,5,6,7,8]
ninja = [None]*9

for i in num:
    ninja[i] = int(input())

combs = list(itertools.combinations(ninja,2))

for i in range(len(combs)):
    c = combs[i]
    first = c[0]
    second = c[1]

    ninja_copy = ninja.copy()
    del ninja_copy[ninja_copy.index(first)]
    del ninja_copy[ninja_copy.index(second)]

    if sum(ninja_copy) == 100:
        ninja_copy.sort()
        print('\n'.join(map(str,ninja_copy)))
        break
