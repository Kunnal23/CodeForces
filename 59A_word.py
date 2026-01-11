s = input()

upper = 0
for ch in s:
    if ch.isupper():
        upper+=1

lower = len(s)-upper
if upper>lower:
    print(s.upper())
else:
    print(s.lower())
