def solution(a, b):
    answer = 0
    if a % 2 == 1 and b % 2 == 1:
        R = a**2 + b**2
        answer += R
    elif a % 2 == 1 or b % 2 == 1:
        R = 2 * (a+b)
        answer += R
    else:
        R = abs(a-b)
        answer += R
    return answer