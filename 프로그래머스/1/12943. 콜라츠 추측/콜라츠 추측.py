def solution(num):
    res = 0
    # num이 1일 경우 0을 return 전처리
    if num == 1:
        return 0
    # 500번 반복
    for _ in range(500):
        # num이 짝수라면 num을 2로 나눈다.
        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = (num * 3) + 1
        res += 1 
        if num == 1:
            return res
        
        
    if res >= 500 and num != 1:
        return -1