t = int(input())


for i in range(t):
    number_list = list(input())
    jumsu = 0
    sum_jumsu = 0
    for ox in number_list:
        if ox == 'O':
            jumsu +=1
        else:
            jumsu = 0
        sum_jumsu += jumsu
    print (sum_jumsu)