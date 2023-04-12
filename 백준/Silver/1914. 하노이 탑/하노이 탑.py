import sys
input = sys.stdin.readline

n = int(input())

def han_52(n,s,m,e):
    if n == 1:
        print(s,e,sep=" ")
    elif n > 1:
        han_52(n-1,s,e,m) #s에서 m으로 이동
        han_52(1,s,m,e) #s에서 e로 이동
        han_52(n-1,m,s,e) #m에서 e로 이동

print(2**n-1)
if (n <= 20):
    han_52(n,1,2,3) # 1에서 3으로 이동 =(s에서 e로 이동시켜봐)
