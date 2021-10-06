# 개리맨더링 2

def cal_people(_r, _c, _d1, _d2):
    people_list = [0] * 5
    vote_boundary = set()
    left = 0
    right = 0
    for l in range(_d1 + _d2 + 1):
        for _ in range(_c + left, _c + right + 1):
            vote_boundary.add((_r+l, _))
        if l < _d1:
            left -= 1
        else:
            left += 1

        if l < _d2:
            right += 1
        else:
            right -= 1
    for i in range(size):
        for j in range(size):
            if (i, j) in vote_boundary:
                people_list[4] += people[i][j]
            else:
                if i < _r + _d1 and j <= _c:
                    people_list[0] += people[i][j]
                elif i <= _r + _d2 and _c < j:
                    people_list[1] += people[i][j]
                elif _r + _d1 <= i and j < _c - _d1 + _d2:
                    people_list[2] += people[i][j]
                else:
                    people_list[3] += people[i][j]
    if 0 in people_list:
        return False
    else:
        return max(people_list) - min(people_list)


size = int(input())
people = [list(map(int, input().split())) for _ in range(size)]
min_diff = 987654321
for r in range(size):
    for c in range(size):
        for d1 in range(1, c + 1):
            for d2 in range(1, size - c):
                if r + d1 + d2 < size:
                    ans = cal_people(r, c, d1, d2)
                    if ans:
                        if ans < min_diff:
                            min_diff = ans
ans = cal_people(2, 2, 1, 1)
print(min_diff)
