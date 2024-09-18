def solution(array):
    answer = 0
    dic = {}
    
    # array를 각 숫자가 몇개있는지 dic형 자료로 만들기
    for i in array:
        i = str(i)
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    maximum_val = max(dic.values())
    cnt = 0
    
    for key, val in dic.items():
        if val == maximum_val:
            cnt += 1
            answer = key
    if cnt >= 2:
        return -1
    if cnt == 1:
        return int(answer)