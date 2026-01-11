str1 = input().strip()

nums = list(map(int,str1.split("+")))
nums.sort()
nums = list(map(str,nums))
print("+".join(nums))