def solution(rny_string):
    answer = ''
    if 'm' in rny_string :
        answer = rny_string.replace('m','rn')
    else:
        answer = rny_string
        
    return answer