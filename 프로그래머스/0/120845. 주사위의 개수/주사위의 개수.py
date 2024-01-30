def solution(box, n):
    temp_h = box[0] // n 
    temp_c = box[1] // n 
    temp_r = box[2] // n
    answer = temp_h * temp_c * temp_r
    return answer