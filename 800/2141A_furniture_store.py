t = int(input())
for _ in range(t):
    n = int(input())
    sofas = list(map(int,input().split()))
    min_price = float('inf')
    ans = []
    for i in range(n):
        if sofas[i]>min_price:
            ans.append(i+1)
        else:
            min_price = sofas[i]
    print(len(ans))
    print(*ans)