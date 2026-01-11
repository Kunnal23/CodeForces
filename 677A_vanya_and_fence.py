n,h = map(int,input().split())
a = list(map(int,input().split()))

width = 0
for val in a:
    if val<=h:
        width+=1
    elif val>h:
        width+=2
print(width)