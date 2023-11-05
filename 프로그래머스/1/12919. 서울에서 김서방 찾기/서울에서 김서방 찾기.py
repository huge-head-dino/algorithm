def solution(seoul):
    answer = 0
    for idx, val in enumerate(seoul):
        if val == "Kim":
            num = idx
    answer = "김서방은 " + str(num) + "에 있다"
    return answer