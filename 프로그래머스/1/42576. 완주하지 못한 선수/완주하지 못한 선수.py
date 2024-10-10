def solution(participant, completion):
    hash_dict = {}
    sum_hash = 0
    
    for i in participant:
        # 주소값을 key로 삼아 dict 채워넣기
        hash_dict[hash(i)] = i
        # 주소값 저장
        sum_hash += hash(i)
    
    for j in completion:
        # 얻어낸 주소값을 sum_hash에서 뺴기
        sum_hash -= hash(j)

    return hash_dict[sum_hash]  