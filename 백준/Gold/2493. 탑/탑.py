# 왼쪽부터 읽는다고 가정했을 때
N = int(input())  # 탑의 개수
top_list = list(map(int, input().split()))  # 탑 리스트
stack = [] # 최댓값을 저장할 스택
answer = [] # 레이저를 수신한 탑의 위치(인덱스)를 저장할 리스트

for i in range(N): # 이 for문에서는 각 탑의  레이저 수신 여부를 판단
    while stack: # 스택이 비어있지 않을 때까지 루프 실행
        if stack[-1][1] > top_list[i]:  # 스택의 맨 위에 있는 탑이 현재 탑보다 높이가 작다면
            answer.append(stack[-1][0] + 1) # 현재 탑에서 레이저가 수신가능한 상황/
                                            # 스택에서 탑을 제거하면서 가장 왼쪽에 있는 탑의 위치를 asnwer에 추가
                                            # 그리고 while 루프를 종료하기 위해 break 실행
            break
        else: # 스택의 맨 위에 있는 탑이 현재 탑보다 높이가 높은 경우. 현재 탑에서 레이저가 수신되지 X
              # 따라서 스택에서 탑을 제거
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, top_list[i]])  # 인덱스, 값

print(" ".join(map(str, answer)))