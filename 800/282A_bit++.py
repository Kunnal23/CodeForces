n = int(input())
x = 0
for _ in range(n):
    a = input()
    if "++" in a:
        x+=1
    elif "--" in a:
        x-=1
print(x)
