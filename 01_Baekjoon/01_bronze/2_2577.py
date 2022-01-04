a = int(input())
b = int(input())
c = int(input())

num = a * b * c

num_list = [0] * 10

for n in str(num):
    num_list[int(n)] += 1

for i in range(10):
    print(num_list[i])