n = int(input())

q = n//5
rem = n%5

if rem:
    print(q+1)
else:
    print(q)