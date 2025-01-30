from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    ch = {word:0 for word in words}
    ch[begin] = 1
    Q = deque()
    Q.append(begin)

    Lv = 0
    
    while Q:
        for c in range(len(Q)):
            stand = Q.popleft()
            print(stand)
            if stand == target:
                return Lv
            for compare in words:
                stand_list = list(stand)
                compare_list = list(compare)
                cnt = 0
                # 1글자 차이 나는건지 비교하기
                for i in range(len(stand_list)):
                    if stand_list[i] != compare_list[i]:
                        cnt += 1
                    if cnt >= 2:
                        break
                if cnt == 1 and ch[compare] == 0:
                    Q.append(compare)
                    ch[compare] = 1
        Lv += 1
                        
