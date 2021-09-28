words = [input() for _ in range(int(input()))]
tmp = set(words)
words = list(tmp)
words.sort(key=lambda x: (len(x), x))
print(*words, sep="\n")