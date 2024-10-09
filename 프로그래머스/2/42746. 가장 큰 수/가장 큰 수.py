from functools import cmp_to_key
def compare(a,b):
    if int(a + b) < int(b + a):
        return -1
    elif int(a + b) > int(b + a):
        return 1
    else:
        return 0
def solution(numbers):
    answer = ''
    numbers = sorted(map(str,numbers), key= cmp_to_key(compare),reverse= True)
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        answer = '0'
    return answer