n = int(input())
max_cap = 0
curr = 0
for i in range(n):
    a,b = map(int,input().split())
    curr = curr-a+b
    max_cap = max(max_cap,curr)
print(max_cap)
