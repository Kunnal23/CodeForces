n = int(input())
count = 1
prev = int(input())
for i in range(1,n):
    curr = int(input())
    if prev != curr:
        count+=1
        prev = curr
print(count)