n = int(input())

p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))

levels = set(p1[1:])
levels.update(p2[1:])

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
