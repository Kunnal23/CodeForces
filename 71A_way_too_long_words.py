n = int(input())

for _ in range(n):
    word = input()
    word_len = len(word)
    if word_len>10:
        print(word[0]+str(word_len-2)+word[-1])
    else:
        print(word)