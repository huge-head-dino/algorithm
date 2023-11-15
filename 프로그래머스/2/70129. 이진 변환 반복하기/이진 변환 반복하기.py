def solution(s):
    answer = []
    repeat_cnt = 0
    zero_cnt = 0
    
    while True:
        if s == '1':                 # s가 1이면 반복을 종료한다,
            break
        zero_cnt += s.count('0')    # 0의 갯수를 세서 cnt에 넣어놓는다.
        s = s.replace('0','')       # 0을 공백으로 대체한다.
        s = bin(len(s))[2:]        # s를 2진법으로 바꾸고 다시 반복하기 위해 위로 보냄
        
        repeat_cnt += 1
        
            
    answer = [repeat_cnt,zero_cnt]
    return answer