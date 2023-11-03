def solution(arr):
    answer = []
    for i in arr:
        if 50 <= i and i % 2 == 0:
            a = i / 2
            answer.append(a)
        elif i < 50 and i % 2 == 1:
            b = i * 2
            answer.append(b)
        else:
            answer.append(i)
    return answer