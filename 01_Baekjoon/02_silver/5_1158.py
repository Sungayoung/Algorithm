people, K = tuple(map(int, input().split()))

Josephus = []
num_list = []

for i in range(1, people+1):
    num_list.append(i)
idx = K-1
Josephus.append(num_list.pop(idx))

while len(num_list) != 0:
    # 현재 탐색한 idx값은 제거되었기 때문에 그 값을 포함 K-1을 더해준다
    idx = (idx + K-1) % len(num_list)
    Josephus.append(num_list.pop(idx))


result = ", ".join(str(i) for i in Josephus)
print("<", result, ">", sep="")
