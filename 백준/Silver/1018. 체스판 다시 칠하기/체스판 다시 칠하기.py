import sys
input = sys.stdin.readline

N,M = map(int, input().split())
chess_board = []
res = []

for _ in range(N):
    chess_board.append(input())

for i in range(N-7):
    for j in range(M-7): # 8*8로 자르기 위해서  -7
        retouch_W = 0 # 흰색으로 시작
        retouch_B = 0 # 검은색으로 시작
        for a in range(i,i+8): #시작하는 지점
            for b in range(j,j+8): #시작하는 지점
                if (a+b)%2==0: # 짝수인 경우
                    if chess_board[a][b]!='W': # 흰색이 아니고 검정색이면
                        retouch_W += 1 # 흰색으로 칠하는 갯수
                    else: # 검정색이 아니고 흰색이라면
                        retouch_B += 1 # 검정색으로 칠하는 갯수
                else: # 홀수인경우
                    if chess_board[a][b]!='W': # 흰색이 아니고 검정색이면
                        retouch_B += 1 # 검정으로 칠하는 갯수
                    else:
                        retouch_W += 1 # 흰색으로 칠하는 갯수

        res.append(retouch_W) # 화이트로 시작할 때 경우의 수
        res.append(retouch_B) # 블랙으로 시작할 때 경우의 수

print(min(res))
                        



