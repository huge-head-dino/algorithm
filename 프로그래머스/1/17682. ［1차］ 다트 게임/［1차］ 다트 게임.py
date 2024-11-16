import re
def solution(dartResult):
    answer = []
    # 1. 하나 이상의 숫자(1자리 또는 여러자리) : \d+
    # 2. [SDT] 다음 중 하나의 문자
    # 3. [*#]? # or *가 0번 또는 1번 나타남
    
    # (1) 정규표현식으로 썰어주기
    pattern = r"(\d+[SDT][*#]?)"
    matches = re.findall(pattern, dartResult)
    
    # (2) temp에 2차원배열로 각 샷 넣기 
    temp = []
    for i in matches:
        # (2-1) 10 예외처리하기
        pattern = r'\d+|\w+|[^\w]'
        res = re.findall(pattern,i)
        temp.append(res)   
    print(temp)
    # (3) 점수 계산하기
    for c in range(0,3):
        point = int(temp[c][0])
        if temp[c][1] == 'S':
            point = point ** 1
        elif temp[c][1] == 'D':
            point = point ** 2
        elif temp[c][1] == 'T':
            point = point ** 3
        
        # (4) 특수 케이스
        if len(temp[c]) == 3:
            if temp[c][2] == '#':
                point *= (-1)
            elif temp[c][2] == '*':
                if answer:
                    answer[-1] = answer[-1] * 2
                point *= 2
        answer.append(point)
    
    answer = sum(answer)
    return answer