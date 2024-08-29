def solution(number):
    answer = 0
    number = list(number)
    for i in number:
        answer += int(i)
    sol = answer % 9
    return sol