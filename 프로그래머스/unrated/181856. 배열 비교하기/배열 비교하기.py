def solution(arr1, arr2):
    answer = 0
    s1 = sum(arr1)
    s2 = sum(arr2)
    l1 = len(arr1)
    l2 = len(arr2)
    
    for i in arr1:
        if l1 > l2:
            answer = 1
        elif l1 < l2:
            answer = -1
        else:
            if s1 > s2:
                answer = 1
            elif s1 < s2:
                answer = -1
            else:
                answer = 0
    return answer