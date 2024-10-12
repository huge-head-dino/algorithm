def solution(answers):
    answer = []
    stand = len(answers)
    
    # 1: first_loop = 5
    first_way = [1,2,3,4,5]
    first_loops = stand // 5
    first_add = stand % 5
    first_ans = first_way * first_loops
    first_slice = first_way[0:first_add]
    
    first_ans.extend(first_slice)
    
    # 2: second_loop = 8
    second_way = [2,1,2,3,2,4,2,5]
    second_loops = stand // 8
    second_add = stand % 8
    second_ans = second_way * second_loops
    second_slice = second_way[0:second_add]
    
    second_ans.extend(second_slice)
    
    # 3: third_loop = 10
    third_way = [3,3,1,1,2,2,4,4,5,5]
    third_loops = stand // 10
    third_add = stand % 10
    third_ans = third_way * third_loops
    third_slice = third_way[0:third_add]
    
    third_ans.extend(third_slice)
    
    first = 0
    second = 0
    third = 0
    
    for i in range(len(answers)):
        if answers[i] == first_ans[i]:
            first += 1
        if answers[i] == second_ans[i]:
            second += 1
        if answers[i] == third_ans[i]:
            third += 1
    
    
    result = []
    result.append(first)
    result.append(second)
    result.append(third)
    
    
    real_answer = []
    
    if max(result) == first:
        real_answer.append(1)
    if max(result) == second:
        real_answer.append(2)
    if max(result) == third:
        real_answer.append(3)
        
    return real_answer