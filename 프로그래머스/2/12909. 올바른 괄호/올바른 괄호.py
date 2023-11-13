from collections import deque
def solution(s):
    answer = True
    # open_arr = []
    # close_arr = []
    # 괄호 수가 짝수가 아니라면 예외처리
    if len(s) % 2 != 0:
        return False
    # 시작이 닫는 괄호거나 끝이 여는 괄호면 예외처리
    if s[0] == ')':
        return False
    if s[-1] == '(':
        return False
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

