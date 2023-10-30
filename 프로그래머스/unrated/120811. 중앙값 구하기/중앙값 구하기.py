import math
def solution(array):
    answer = 0
    array.sort()
    a = len(array) / 2
    res = math.floor(a)
    answer = array[res]
    
    return answer