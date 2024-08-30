def solution(num, k):
    answer = 0
    num = str(num)
    num = list(num)
    if str(k) not in num:
        return -1
    for i,val in enumerate(num):
        if str(k) == val:
            answer = i + 1
            return answer