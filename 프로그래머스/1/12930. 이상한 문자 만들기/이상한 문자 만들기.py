def solution(s):
    answer = ''
    ing_list = s.split(' ')
    for i in ing_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                # lower처리 안해보기
                answer += i[j].lower()
        answer += ' '
    answer = answer[:-1]
    return answer
            
            