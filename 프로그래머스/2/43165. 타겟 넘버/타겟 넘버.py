
def solution(numbers, target):
  # BFS
    # 1. 준비 단계
    Q = [0]
    cnt = 0
    
    # 2. 0을 기준으로 + - 분화
    for num in numbers:
        temp = []
        for add in Q:
            temp.append(add + num)
            temp.append(add - num)
        Q = temp
    
    # 3. target계산
    for i in Q:
        if i == target:
            cnt += 1
    return cnt   