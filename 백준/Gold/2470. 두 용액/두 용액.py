import sys
input = sys.stdin.readline

# 입력받고 정렬하기
N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

# 이중포인터 설정
start = 0
end = N-1

# 비교할 기준값(젤 큰값으로), 정답을 출력할 빈리스트 형성
answer = 2e9
result = []

# 이중포인터로 탐색 진행
while start < end:
    pl = liquid[start]
    pr = liquid[end]
    mid = pl + pr
    # 두 용액의 합이 0과 가장 가까운 용액을 result에 담아준다.
    if abs(mid) < abs(answer):
        answer = abs(mid)
        result = [pl,pr]

    # 두 용액의 합이 0보다 작다면 오름차순으로 정렬되어 있기 때문에
    # pl값 즉, -값을 조금 줄여준다.
    if mid < 0:
        start += 1
    # 마찬가지로 두 용액의 합이 0보다 크면,
    # pr 값 즉, +값을 조금 줄여준다.
    else:
        end-= 1

print(result[0],result[1])


    

