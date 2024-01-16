def solution(arr, delete_list):
    answer = arr.copy()
    for i in arr:
        for j in delete_list:
            if i == j:
                answer.remove(i)
    return answer