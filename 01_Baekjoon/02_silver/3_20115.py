# 에너지 드링크

N = int(input())

drink = list(map(int, input().split()))
drink.sort()
result = drink[-1]

for i in range(N-1):
    result += drink[i] / 2
print(result)
