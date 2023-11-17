def solution(brown, yellow):
    answer = []
    div = []
    target = brown + yellow
    for i in range(1,target+1):
        if target % i == 0:
            div.append(i)
    for j in div:
        garo = target // j 
        print(garo,j)
        if (garo-2) * (j -2) == yellow:
            answer.append(garo)
            answer.append(j)
            break
    return answer
# 완전탐색이니까 일단 brown과 yellow의 값을 더한다.
# 그 값을 곱해서 나오는 약수들을 조사한다.
# yellow의 법칙 : 각 return값에서 -2씩 했을 경우 yellow 값이 나와야 함

