def solution(order):
    cnt = 0
    order = str(order)
    order = list(order)
    for i in order:
        i = int(i)
        if i == 0:
            continue
        if i % 3 == 0:
            cnt += 1
    return cnt