import sys
input = sys.stdin.readline

num = int(input())
alpha_list=[]

for i in range(num):
    alpha = input()
    alpha_list.append(alpha)
    
alpha_list.sort()
alpha_list.sort(key=len)

hihi = list(dict.fromkeys(alpha_list))

for i in hihi:
    print(i,end='')