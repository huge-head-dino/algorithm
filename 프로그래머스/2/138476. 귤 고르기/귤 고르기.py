def solution(k, tangerine):
    answer = 0
    dp = {}
    # 딕셔너리를 사용해서 시간복잡도를 줄여주기
    for i in tangerine:
        if i in dp:
            dp[i] += 1
        else:
            dp[i] = 1
    dp =  dict(sorted(dp.items(), key = lambda x: x[1], reverse = True))
    for i in dp: # dict를 돌리면, key값을 반환한다는 사실!
        if k <= 0:
            return answer
        else:
            k-= dp[i]
            answer += 1       
    return answer