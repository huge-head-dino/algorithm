def solution(todo_list, finished):
    answer = []
    for idx, val in enumerate(finished):
        if val == False:
            answer.append(todo_list[idx])
    return answer