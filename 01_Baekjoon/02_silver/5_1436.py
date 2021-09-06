
N = int(input())

cnt = 0
num = 0
while True:
    if cnt == N:
        break
    num += 1
    if '666' in str(num):
        cnt += 1

print(num)