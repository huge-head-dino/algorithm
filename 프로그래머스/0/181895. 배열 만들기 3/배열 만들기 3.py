def solution(arr, intervals):
    answer = []
    sol = []
    for i in intervals:
        answer.append(arr[i[0]:i[1]+1])
    for j in answer:
        for k in j:
            sol.append(k)
    return sol