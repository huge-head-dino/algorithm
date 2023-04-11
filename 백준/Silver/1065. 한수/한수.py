MJ= int(input())

result = 0

for i in range(1,MJ+1):
    if 1 <= i <= 99:
        result += 1
    elif 100 <= i <= 1000:
        a = list(str(i))
        if int(a[0])-int(a[1]) == int(a[1])-int(a[2]):
            result +=1
        else:
            pass
    else:
        pass

print(result)

