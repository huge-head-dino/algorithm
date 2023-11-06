import math
def solution(n, m):
    answer = []
    # 최소공배수
    # 최소공배수는 n과 m을 나누는 수 중 가장 커야한다.
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            # 핵심! break를 걸어주지 않으면, 그냥 공배수도 들어가게 된다.
            break
    # 최대공약수
    # 최대공약수는 n과 m 모두 나누어지는 수 중 가장 작아야한다.
    for i in range(max(n,m), n * m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            # 핵심! break를 걸어주지 않으면, 그냥 공약수도 들어가게 된다.
            break
            
    return answer