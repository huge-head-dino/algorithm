from collections import deque
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i == ')':
            return False
        if i =='(':
            stack.append(i)
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
    
    return answer

