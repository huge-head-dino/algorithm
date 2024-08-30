def solution(strArr):
    temp = strArr.copy()
    for i, val in enumerate(strArr):
        if 'ad' in val:
            temp.remove(val)
    return temp