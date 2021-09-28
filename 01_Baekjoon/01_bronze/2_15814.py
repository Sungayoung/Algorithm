# 야바위 대장

words = list(input())

for _ in range(int(input())):
    A, B = map(int, input().split())
    words[A], words[B] = words[B], words[A]

print("".join(words))