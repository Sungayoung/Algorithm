# 직사각형을 만드는 방법

square = int(input())
cnt = 0
prev = 0
for num in range(1, int(square ** 0.5) + 1):
    cnt += square // num - prev
    prev = num
print(cnt)