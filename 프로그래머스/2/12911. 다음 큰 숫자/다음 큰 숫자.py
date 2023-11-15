def solution(n):
    answer = n
    bench = bin(n)
    bench_num = bench.count('1')
    while True:
        answer += 1  #이진수를 문자열로 구분해서 처리하겠다는 생각보다는 1씩 더해서 완전탐색하겠다는 마인드
        answer_bin = bin(answer)
        num = answer_bin.count('1')
        
        if int(num) == bench_num:
            return answer