def solution(cipher, code):
    answer=''
    cipher = list(cipher)
    for i,val in enumerate(cipher):
        answer_index = i + 1
        if answer_index // code > 0 and answer_index % code == 0:
            answer += cipher[i]
    return answer