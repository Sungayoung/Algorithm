no_hear, no_see = tuple(map(int, input().split()))

no_hear_list = set()
no_see_list = set()
for _ in range(no_hear):
    no_hear_list.add(input())

for _ in range(no_see):
    no_see_list.add(input())

no_hear_see_list = list((no_hear_list & no_see_list))
no_hear_see_list.sort()

print(len(no_hear_see_list))
print(*no_hear_see_list, sep='\n')