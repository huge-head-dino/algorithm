import sys
input = sys.stdin.readline

#입력받기
n,m = map(int,input().split())
graph = []
for _ in range(n):
    muni = list(input().strip())
    graph += [muni]

count = 0


for i in range(n):
    compare = ''
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != compare:
                count+=1
#비교대상을 현재 반복중인 요소로 교체
        compare = graph[i][j]


for i in range(m):
    compare = ''
    for j in range(n):
        if graph[j][i] == '|':
            if graph[j][i] != compare:
                count+=1
#비교대상을 현재 반복중인 요소로 교체
        compare = graph[j][i]

print(count)


        
    

