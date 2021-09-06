# 서든어택 3
import sys

input = sys.stdin.readline
N = int(input())

tmp = list(map(int, input().split()))
jun = tmp[0]
power = tmp[1:]
power.sort()
result = "Yes"
for p in power:
    if jun > p:
        jun += p
    else:
        result = "No"
        break

print(result)
