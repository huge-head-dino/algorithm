
from collections import deque
import math

def solution(progresses, speeds):
    # 남은 process 확인하기
    rest = []
    for i in progresses:
        process = 100 - i
        rest.append(process)
        
    # zip으로 묶어서 필요한 날짜 계산하기
    days = [] 
    for a,b in zip(rest,speeds):
        day = math.ceil(a / b)
        days.append(day)
    
    # 최종처리하기
    days = deque(days)
    answer = []
    cnt = 0
    
    # print(days)
    while days:
        cnt = 0
        out = days.popleft()
        cnt += 1
        if not days:
            answer.append(cnt)
            break
        else:
            while out >= days[0]:
                days.popleft()
                cnt += 1
                if not days:
                    answer.append(cnt)
                    break
            else:
                answer.append(cnt)
    return answer
        
    