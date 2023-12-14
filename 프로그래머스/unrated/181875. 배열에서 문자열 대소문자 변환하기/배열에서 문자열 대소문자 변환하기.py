def solution(strArr):
    answer = []
    for idx, val in enumerate(strArr):
        if idx % 2 == 0:
            a = strArr[idx].lower()
            answer.append(a)
        else:
            b = strArr[idx].upper()
            answer.append(b)
    return answer