import sys
input = sys.stdin.readline

H,M = map(int,input().split())

if M >=45:
    print(H, M-45)
elif H > 0 and M < 45:
    print(H-1, M+15)
elif H==0:
    print(23, M+15)
