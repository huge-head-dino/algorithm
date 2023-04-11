num = int(input())

x = [None] * num

for i in range(num):
    a = int(input())
    x[i] = a

for i in sorted(x):
    print(i)