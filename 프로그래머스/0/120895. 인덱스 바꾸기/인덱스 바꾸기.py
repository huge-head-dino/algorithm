def solution(my_string, num1, num2):
    L_string = list(my_string)
    temp = L_string.copy()
    L_string[num1] = temp[num2]
    L_string[num2] = temp[num1]
    answer = "".join(L_string)
    return answer