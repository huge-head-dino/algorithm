def solution(s):
    answer = reversed((sorted(s)))
    answer = ''.join(answer)
    return answer