n,k = map(int,input().split())
nums = list(map(int,input().split()))

count = 0
val = nums[k-1]
for num in nums:
    if num<=0 or num<val:
        break
    count+=1

print(count)