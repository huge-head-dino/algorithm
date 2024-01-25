def solution(myString):
    answer = []
    cnt = 0
    for idx, val in enumerate(myString):
        if val == 'x':
            answer.append(cnt)
            cnt = 0
        else:
            cnt += 1
    answer.append(cnt)
    return answer