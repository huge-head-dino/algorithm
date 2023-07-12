import sys
input = sys.stdin.readline

num = list(map(int , input().split()))
A_ele = list(map(int , input().split()))
B_ele = list(map(int , input().split()))

a = set(A_ele)
b = set(B_ele)

jin_a = a - b 
jin_b = b - a

print(len(jin_a)+len(jin_b))