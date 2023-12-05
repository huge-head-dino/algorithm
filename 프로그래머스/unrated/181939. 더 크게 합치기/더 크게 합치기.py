def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    case_1 = int(a+b) 
    case_2 = int(b+a)
    if case_1 >= case_2:
        answer = case_1
    else:
        answer = case_2
        
    return answer