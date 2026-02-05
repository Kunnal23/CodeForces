t = int(input())
for _ in range(t):
    s = input()
    if set(s) == {'a'}:
        print("NO")
        continue

    front = 'a' + s
    if front != front[::-1]:
        print("YES")
        print(front)
    else:
        print("YES")
        print(s+'a')