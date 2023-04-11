T = int(input())

for i in range(T):
    r, s = input().split()
    R=int(r)
    S=list(s)
    part_sum = ''
    for i in S:
        part = i*R
        part_sum += part
    print(part_sum)