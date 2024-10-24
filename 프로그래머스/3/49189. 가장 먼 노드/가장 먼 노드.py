from collections import deque
def solution(n, edge):
    # 1 : 준비
    answer = 0
    edge = sorted(edge)
    distance = [0] * (n+1)
    queue = deque()
    graph = [[] for _ in range(n+1)]
    
    # 2 : 인접리스트 생성
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 3 : 큐에 시작 노드를 넣고 출발
    queue.append(1)
    distance[1] = 1 # 방문한 노드의 거리에 1을 추가하기 위해 애초에 1을 집어넣어주기
    
    # 4: 탐색 시작
    while queue:
        now = queue.popleft()
        for node in graph[now]:                    # 시작노드가 속한 graph에 진입
            if distance[node] == 0:                # 방문한 적 없는 노드라면,
                queue.append(node)                 # 큐에 추가, 방문 했다고 기록은 아랫줄
                distance[node] = distance[now] + 1 # 해당 노드의 거리 + 1
    maxima = max(distance)
    for dist in distance:
        if dist == maxima:
            answer += 1
    return answer