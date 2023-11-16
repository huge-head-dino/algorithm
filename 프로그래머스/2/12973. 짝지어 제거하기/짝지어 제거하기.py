from collections import deque
def solution(s):
    answer = 0
    stack = deque()
    s = list(s)
    for idx, val in enumerate(s):
        if idx == 0:
            stack.append(val)
        else:
            if len(stack) >= 1 and stack[len(stack)-1] == val:
                stack.pop()
            else:
                stack.append(val)
    if len(stack) == 0:
        return 1
    return answer