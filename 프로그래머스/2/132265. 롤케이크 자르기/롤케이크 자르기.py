from collections import Counter, defaultdict
def solution(topping):
    answer = 0
    
    chul_dic = Counter(topping) 
    dong_dic = defaultdict(int)

    for i in topping:
        dong_dic[i] += 1
        if chul_dic[i] == 1:
            chul_dic.pop(i)
        else:
            chul_dic[i] -=1
        
        if len(chul_dic.keys()) == len(dong_dic.keys()):
            answer += 1
    return answer