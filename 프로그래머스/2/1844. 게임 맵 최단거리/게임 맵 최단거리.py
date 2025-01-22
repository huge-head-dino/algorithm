from collections import deque
def solution(maps):
    # 지도 크기 계산
    garo = len(maps[0])  # 가로 길이
    sero = len(maps)     # 세로 길이
    
    # 방문 여부를 기록할 배열
    visited = [[0 for _ in range(garo)] for _ in range(sero)]
    
    # 상하좌우 이동 방향
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # BFS 탐색을 위한 큐 초기화
    Q = deque()
    Q.append((0, 0, 1))  # (x, y, 현재까지의 거리)
    visited[0][0] = 1  # 시작점 방문 처리
    
    # BFS 탐색
    while Q:
        nx, ny, dist = Q.popleft()
        
        # 목표 지점에 도달한 경우
        if nx == (garo - 1) and ny == (sero - 1):
            return dist
        
        # 상하좌우 탐색
        for cos in range(4):
            x = nx + dx[cos]
            y = ny + dy[cos]
            
            # 이동 가능 여부 확인
            if 0 <= x < garo and 0 <= y < sero and maps[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = 1  # 방문 처리
                Q.append((x, y, dist + 1))  # 거리 + 1
    
    # 도달할 수 없는 경우
    return -1
