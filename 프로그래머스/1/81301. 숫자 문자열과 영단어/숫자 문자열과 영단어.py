def solution(s):
    answer = 0
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for idx, val in enumerate(numbers):
        s = s.replace(val,str(idx))
    return int(s)