n = input()
count = 0
for num in n:
    if num in "47":
        count+=1

if count>0 and all(c in '47' for c in str(count)):
    print("YES")
else:
    print("NO")

