import sys
input = sys.stdin.readline

sik = input().strip().split('-')

result = 0
for i in sik[0].split('+'):
    result += int(i)
for i in sik[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)
