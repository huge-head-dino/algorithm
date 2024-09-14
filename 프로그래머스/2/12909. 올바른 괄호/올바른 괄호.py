from collections import deque
def solution(data):
    

    answer = True
    data = deque(data)
    # 애초 성립 안되는 데이터 전처리
    if data[0] == ')':
        answer = False
    
    stack = deque()
    
    for i in data:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.popleft()
    
    if len(stack) == 0:
        answer = True
    else:
        answer = False
    
    return answer