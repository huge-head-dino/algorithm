def solution(clothes):
    kind = {}
    answer = []
    for clo in clothes:
        if clo[1] in kind:
            kind[clo[1]] += 1
        else:
            kind[clo[1]] = 1 
    
    for i in kind.values():
        answer.append(i+1)
    
    # 한종류 밖에 없으면 고대로 리턴
    if len(answer) == 1:
        return answer[0] - 1
    
    cnt = 1
    for i in answer:
        cnt *= i
    result = cnt -1
    
    return result
    
    