# 스위치 켜고 끄기

N = int(input())

switch = list(map(int, input().split()))
for _ in range(int(input())):
    gender, num = map(int, input().split())
    if gender == 1:     # 남학생
        for i in range(num-1, N, num):
            switch[i] = (switch[i] + 1) % 2
    elif gender == 2:
        switch[num - 1] = (switch[num - 1] + 1) % 2
        for i in range(1, N):
            if 0 <= num -1 + i < N and 0 <= num -1- i < N:
                if switch[num-1 + i] == switch[num-1 - i]:
                    switch[num - 1 + i] = (switch[num - 1 + i] + 1) % 2
                    switch[num - 1 - i] = (switch[num - 1 - i] + 1) % 2
                else:
                    break
for i in range(0, N, 20):
    print(*switch[i: i+20], sep=" ")