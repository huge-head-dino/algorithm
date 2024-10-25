from collections import deque
def solution(bandage, health, attacks):
    t, x, y = bandage
    end = attacks[-1][0]
    attacks = deque(attacks)
    cnt = 0
    condition = health
    for i in range(1,end+1):
        button = False
        if i == attacks[0][0]:
            condition -= attacks[0][1]
            attacks.popleft()  # 추후에 빈게 문제 되진 않는지 확인하기
            cnt = 0
            button = True
        if condition < 0:  # 맞아서 죽으면 그대로 죽여
            return -1
        if condition < health and button == False:
            condition += x
            cnt += 1
            if condition > health: # 회복량이 최대체력을 초과할 수 없게 한다.
                condition = health
            if cnt == t:
                condition += y
                if condition > health: # 회복량이 최대체력을 초과할 수 없게 한다. 
                    condition = health
                cnt = 0    # 연속 성공해서 y얻으면 시간 다시 초기화
    if condition > 0:
        return condition
    else:
        return -1