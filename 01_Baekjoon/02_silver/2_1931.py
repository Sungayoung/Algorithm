# 회의실 배정

times = []
for i in range(int(input())):
    times.append(tuple(map(int, input().split())))


times.sort(key=lambda x: (x[1], x[0]))
end = 0
result = 0
for time in times:
    if time[0] >= end:
        end = time[1]
        result += 1

print(result)