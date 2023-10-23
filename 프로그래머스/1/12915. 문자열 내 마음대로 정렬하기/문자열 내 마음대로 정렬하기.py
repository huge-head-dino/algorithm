def solution(strings, n):
    answer = []
    res = strings
    sorted_words = sorted(res, key=lambda x: (x[n],x[0:n],x[n+1:]))
    
    return sorted_words