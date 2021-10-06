# 나이순 정렬

people = []
for _ in range(int(input())):
    tmp = input().split()
    people.append((int(tmp[0]), tmp[1]))

people.sort(key=lambda x: x[0])
for p in people:
    print("{} {}".format(p[0], p[1]))