def solution(start, end_num):
    answer = []
    for i in range(end_num,start+1):
        answer.append(i)
    answer = sorted(answer, reverse = True)
    return answer