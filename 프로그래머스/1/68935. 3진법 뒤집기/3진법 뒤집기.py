def solution(n):
    answer = ''
    
    while n > 0:
        n, remain = divmod(n,3)
        print(n,remain)
        answer += str(remain)
    return int(answer,3)