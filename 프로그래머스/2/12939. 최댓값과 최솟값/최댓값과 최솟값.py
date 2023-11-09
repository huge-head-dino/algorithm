def solution(s):
    answer = ''
    s = s.split()
    s = list(map(int, s))
    s = sorted(s)
    s = list(map(str, s))
    answer += s[0]
    answer += ' '
    answer += s[-1]
    
    return answer