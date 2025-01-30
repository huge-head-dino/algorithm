def DFS(n, com, computers, visited):
    # DFS 방문 처리
    visited[com] = 1
    for connect in range(n): # 변화를 발생시킨다.
        if connect != com and visited[connect] == 0 and computers[com][connect] == 1:
            DFS(n, connect, computers, visited) # com에서 connect로 타고갔기 때문에 connect를 컴으로 바꿔준다

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)] # 2차원 배열이 아니어도 됨. 컴퓨터 한대씩 방문
    for com in range(n):
        if visited[com] == 0: # 방문하지 않은 곳 탐색 시작
            DFS(n, com, computers, visited)
            answer += 1
    return answer
                