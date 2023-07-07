import sys
input = sys.stdin.readline
import re

N = int(input())
M = input()
string = M
numbers = re.findall(r'\d+', string)

real_number = list(map(int,numbers))

res = sum(real_number)

print(res)