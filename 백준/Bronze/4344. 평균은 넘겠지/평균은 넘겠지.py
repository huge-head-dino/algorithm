c = int(input())

for i in range(c):
    jumsu= list(map(int, input().split()))
    sum_jumsu = sum(jumsu[1:])
    av_jumsu= sum_jumsu/(len(jumsu)-1)

    pf = 0
    for i in jumsu[1:]:
        if i > av_jumsu:
            pf += 1
        else:
            pass
    print(format(pf/len(jumsu[1:])*100,".3f")+'%')

