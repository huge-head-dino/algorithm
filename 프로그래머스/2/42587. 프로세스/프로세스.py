from collections import deque
def solution(priorities, location):
    # 사전준비
    priorities = deque(priorities)
    record = list(range(len(priorities))) # 가장 처음의 형태의 index를 기록해놓는다.
    record = deque(record)
    answer_p = []
    answer_s = []
    
    while priorities:
        # 가장 큰 수가 몇번째 인덱스를 가지고 있는지 구해보기
        max_p = max(priorities)
        res = priorities.index(max_p) #res는 현재 list에서 가장 큰 수의 index

        for i in range(res):
            priorities.rotate(-1)
            record.rotate(-1)
        p = priorities.popleft()
        s = record.popleft()
        answer_p.append(p)
        answer_s.append(s)
    ans = answer_s.index(location) + 1
    return ans
    
    