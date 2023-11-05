def solution(absolutes, signs):
    answer = 0
    for idx, val in enumerate(absolutes):
        if signs[idx] == True:
            answer += val
        elif signs[idx] == False:
            answer -= val
    return answer