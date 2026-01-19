k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
count = [0]*(d+1)
if any(x==1 for x in [k,l,m,n]):
    print(d)
else:
    for i in range(k,d+1,k):
        count[i] = 1
    for i in range(l,d+1,l):
        count[i] = 1
    for i in range(m,d+1,m):
        count[i] = 1
    for i in range(n,d+1,n):
        count[i] = 1
    print(sum(count))