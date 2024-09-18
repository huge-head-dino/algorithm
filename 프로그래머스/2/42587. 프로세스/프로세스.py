from collections import deque
def solution(priorities, location):
    answer = 0
    clear = deque()
    clear_dp = deque()
    priorities = deque(priorities)
    
    dp = list(range(len(priorities)))
    for i in range(len(dp)):
        dp[i] = str(i)
    dp = deque(dp)
    print(dp)
    
    # priorities가 존재하면 반복
    while priorities:
        standard = priorities.popleft()
        dp_s = dp.popleft()
        if priorities and standard < max(priorities):
            priorities.append(standard)
            dp.append(dp_s)
            
        else: 
            clear.append(standard)
            clear_dp.append(dp_s)
    
    if str(location) in clear_dp:
        answer = clear_dp.index(str(location)) + 1
    else:
        answer = 0
    
    # 해결 못한 문제점 : location에 주어진 값이 다른 priorities값과 동일하면 어떻게 구별?
    # 지금 standard가 주어진 priorities에서 몇번쨰 location이었는지 확인한다?
    return answer