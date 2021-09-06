T = int(input())
book = {}
for i in range(T):
    temp = input()
    if book.get(temp, 0):
        book[temp] += 1
    else:
        book[temp] = 1

tmp_list = sorted(book.items(), key=lambda x: x[0], reverse=True)
result = sorted(tmp_list, key=lambda x: x[1])
print(result[-1][0])
