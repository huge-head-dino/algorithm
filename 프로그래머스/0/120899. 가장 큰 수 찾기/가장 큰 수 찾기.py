def solution(array):
    answer = []
    M = max(array)
    for idx,val in enumerate(array): 
        if val == M:
            answer.append(val)
            answer.append(idx)
    return answer