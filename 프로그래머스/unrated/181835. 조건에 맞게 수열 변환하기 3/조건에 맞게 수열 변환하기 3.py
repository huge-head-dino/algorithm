def solution(arr, k):
    answer = []
    if k % 2 != 0:
        for i in arr:
            a = i * k
            answer.append(a)
    else:
        for j in arr:
            b = j + k
            answer.append(b)
    return answer