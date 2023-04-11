x = int(input())

y = int(x % 4) 
z = int(x % 100)
g = int(x % 400)

if y == 0 and z != 0 or g == 0 :
    print(1)
else:
    print(0)