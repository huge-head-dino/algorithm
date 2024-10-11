def solution(citations):
    answer = 0
    citations = sorted(citations)
    
    
    if citations[-1] == 0:
        return 0
    
    for i in range(0,len(citations)):
        entire = len(citations)
        pass_idx = len(citations[0:i])
        if citations[i] >= (entire - pass_idx):
            return entire - pass_idx