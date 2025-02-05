from collections import defaultdict
def solution(tickets):
    answer = []
    t_dict = defaultdict(list)
    
    # key: 출발지, value: 목적지인 딕셔너리 만듦
    for s, e in tickets:
        t_dict[s].append(e) # t_dict[s]만 선언하면 빈리스트가 val로 할당, append까지 해야함
    
    # 목적지 기준 내림차순 정렬(맨 오른쪽 것을 pop해서 쓸 예정이다. 알파벳 순서 상 가장 앞선 것)
    for t_key in t_dict.keys():
        t_dict[t_key].sort(reverse = True)
    
    answer = []
    route = ['ICN']
    
    while route:
        now = route[-1]
        if now not in t_dict or len(t_dict[now]) == 0:
            answer.append(route.pop())
        else:
            route.append(t_dict[now].pop())
    return answer[::-1]
