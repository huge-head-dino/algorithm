from collections import Counter
def solution(N, stages):    
    stages = sorted(stages,reverse = True)
    standard = len(stages)
    dicts = dict()
    for i in range(1,N+2):
        if i in stages:
            dicts[i] = stages.count(i)
        else:
            dicts[i] = 0
    dicts = dict(sorted(dicts.items(), key = lambda x: x[0]))
    fails = dicts.copy()
    
    for key,val in dicts.items():
        if val == 0:
            continue
        fails[key] = val/standard
        standard -= val

    fails = dict(sorted(fails.items(), key = lambda x: x[1],reverse = True))
    answer = []
    for c in fails.keys():
        if c == N+1:
            continue
        answer.append(c)
    return answer
