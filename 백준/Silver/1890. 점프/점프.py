import sys
input = sys.stdin.readline

N = int(input())

matrix = [list(map(int,input().split()))for i in range(N)]

dp = [[0]*N for i in range(N)]
dp[0][0] = 1 

for i in range(N):
    for j in range(N):
        jump = matrix[i][j]
        
        #matrix를 다 탐색했으면 = 가장 오른쪽 아래 도착했으면 종료
        #dp[i][j]가 0이 아니라는 것은 앞서 점프를 뛰어서 착지한 위치(1을 기록해놨으니까)에서
        #도착점까지 계속 점프를 이어간다는 것.

        if dp[i][j] != 0 and matrix[i][j] != 0: 
            
            if i + jump < N: # N보다 작으면 아래(행)로 jump
                dp[i+jump][j] += dp[i][j]
            if j + jump < N: # N보다 작으면 오른쪽(열)으로 jump
                dp[i][j+jump] += dp[i][j]
print(dp[-1][-1])
            