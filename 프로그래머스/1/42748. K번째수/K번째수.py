def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0] - 1
        j = c[1]
        k = c[2] - 1
        A = array[i:j]
        A = sorted(A)
        answer.append(A[k])
    return answer