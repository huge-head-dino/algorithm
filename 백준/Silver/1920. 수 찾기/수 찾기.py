import sys
input = sys.stdin.readline

N = int(input())
N_num = sorted(list(map(int,input().split())))
are_you_in = int(input())
are_you_in_list = list(map(int,input().split()))

def AYI(N_num,x):
    #탐색할 범위를 저장하는 변수 start,end
    #리스트 전체를 범위로 탐색 시작 (0~len(N_num)-1)
    start = 0
    end = len(N_num)-1

    while start <= end: # 탐색할 범위가 남아 있는 동안 반복
        mid = (start+end)//2 # 탐색범위의 중간 위치(퀵소트의 피봇같은 것)
        if x == N_num[mid]: # 발견!
            return 1
        elif x> N_num[mid]: # 찾는 값이 더 크면 오른쪽으로 범위를 좁혀 계속 탐색
            start = mid + 1
        else:               # 찾는 값이 더 작으면 왼쪽으로 범위를 좁혀 계속 탐색
            end = mid - 1
    return 0

for i in are_you_in_list:
    print(AYI(N_num,i))