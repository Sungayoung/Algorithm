N = int(input())

num_list = list(map(int, input().split()))

# 1 2 3 4 6 12

print(min(num_list) * max(num_list))