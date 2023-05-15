import sys
input = sys.stdin.readline

N= int(input())
T_list=[]
P_list=[]

for _ in range(N):
    T,P = map(int, input().split())
    T_list.append(T)
    P_list.append(P)


dp=[]
for i in range(N+1):
    dp.append(0)

for i in range(N-1, -1, -1): # step을 -1로해서 뒤에서부터 리스트 작성
    if T_list[i]+i > N:# 상담에 필요한 일수가 퇴사일을 넘어가면
       dp[i] = dp[i+1] # 다음날 값을 그대로 가져옴
    else:
       dp[i] = max(dp[i+1],dp[T_list[i]+i] + P_list[i]) # 오늘 상담을 안할 경우와 상담을 할 경우 중 더 큰 값

print(dp[0])