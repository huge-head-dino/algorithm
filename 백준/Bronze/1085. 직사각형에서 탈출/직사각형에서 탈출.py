x,y,w,h = map(int, input().split())


b = int(w-x)
c = int(h-y)

a = [x,y,b,c]
print(min(a))