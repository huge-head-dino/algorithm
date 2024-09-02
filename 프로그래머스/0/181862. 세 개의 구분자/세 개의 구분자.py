def solution(myStr):
    answer = []
    temp = []
    
    # ABC로만 이뤄졌으면 EMPTY출력
    if all(j in 'abc' for j in myStr):
        return ["EMPTY"]
    
    for i in myStr:
        if i in 'abc':
            if temp:
                piece = ''.join(temp)
                answer.append(piece)
                temp = []
        else:
            temp.append(i)
    # 마지막 temp에 남아있는 부분을 처리해주고 마무리
    if temp:
        piece = ''.join(temp)
        answer.append(piece)
    
    return answer
            
    