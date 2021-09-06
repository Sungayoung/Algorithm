T = int(input())
room_n = []
for test_case in range(T):
    room_n.append(int(input()))

for n in room_n:
    room = [0 for i in range(n)]
    for i in range(1, n+1):         # 배수 n = 5
        for j in range(i-1, len(room), i):
            room[j] = (room[j] + 1) % 2
        #     print(j, end=' ')
        # print()
    print(room.count(1))
            