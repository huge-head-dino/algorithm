def solution(num_list):
    gop = 1
    zegop = 0
    for i in num_list:
        gop *= i
    print(gop)
    zegop = sum(num_list) 
    if gop < zegop**2:
        return 1
    else:
        return 0