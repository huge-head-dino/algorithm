def solution(name, yearning, photo):
    answer = []
    res = 0
    # photo에 있는 녀석들이 name에 있는지 in으로 확인한다
    # 그리고 그 name에 해당하는 녀석들을 yearning으로 환산해서 점수를 더한다.
    for i in photo: # 일차원배열만 끄집어내기 즉,i는 일차원배열
        for j in i:             # 원소=문자열 끄집어내기 즉,j는 문자열
            if j in name:
                idx = name.index(j)
                res += yearning[idx]
        else:
            answer.append(res)
            res = 0
    return answer