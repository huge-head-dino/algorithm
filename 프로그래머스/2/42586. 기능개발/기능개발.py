from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    queue = deque()
    # 필요한 작업 일수를 계산해서 따로 queue에 담기
    for i in range(len(speeds)):
        need_day = math.ceil((100 - progresses[i]) / speeds[i])
        queue.append(need_day)
    print(queue)
    
    # queue에서 원소 다 빠질 때까지 반복하는 while
    while queue:
        standard = queue.popleft()
        cnt = 1
        # 막혀있던 값이 나갈 때, 같이 나갈 값들 처리하는 while
        while queue and standard >= queue[0]:
            queue.popleft()
            cnt += 1
        answer.append(cnt)
    return answer