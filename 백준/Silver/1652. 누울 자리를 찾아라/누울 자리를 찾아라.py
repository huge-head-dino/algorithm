import sys
input = sys.stdin.readline

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]

res = [0,0]
for i in range(N):
    leng_r , leng_c = 0,0
    for j in range(N):
        if board[i][j] == '.':
            leng_r += 1
        else:
            leng_r = 0
        if leng_r == 2:
            res[0]+=1
    
        if board[j][i] == '.':
            leng_c +=1
        else:
            leng_c = 0
        if leng_c ==2:
            res[1]+=1
print(*res)