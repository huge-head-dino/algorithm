def solution(arr):
    answer = 0
    stack = []
    for i in arr:
        # 비어 있을 때, pop erorr 방지
        if len(stack)== 0:
            stack.append(i)
            continue
            
        c = stack.pop()
        if i == c:
            stack.append(c)
            continue
        elif i != c:
            stack.append(c)
            stack.append(i)
    
    return stack