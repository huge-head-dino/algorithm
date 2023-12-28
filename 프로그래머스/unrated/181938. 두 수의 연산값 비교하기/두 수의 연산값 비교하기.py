def solution(a, b):
    answer = 0
    a1 = str(a)
    b1 = str(b)
    if int(a1+b1) >= 2*a*b:
        answer = int(a1+b1)
    else:
        answer = 2*b*a
    return answer