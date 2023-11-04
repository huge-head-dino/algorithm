def solution(a, b):
    answer = 0
    if a < b :
        answer = sum(list(range(a,b+1)))
    elif a == b:
        answer = a
    elif b < a:
        answer = sum(list(range(b,a+1)))

    return answer