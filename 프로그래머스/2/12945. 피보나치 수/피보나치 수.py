
def solution(n):
    answer = []
    for i in range(n+1):
        if i==0 or i==1:
            answer.append(i)
        else:
            fib = answer[i-2] + answer[i-1]
            answer.append(fib % 1234567)
    return answer[-1]