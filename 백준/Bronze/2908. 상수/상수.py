park, mj = map(int,input().split())

PARK = list(str(park))
MJ = list(str(mj))

a= list(reversed(PARK))
b= list(reversed(MJ))

result_a = ''.join(a)
result_b = ''.join(b)

c = int(result_a)
d = int(result_b)

if c > d:
    print(c)
else:
    print(d)



