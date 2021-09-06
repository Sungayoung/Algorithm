# a: 직사각형, b: 선분, c: 점, d: 공통부분이 없음
for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    result = "a"
    # 공통부분이 없는 경우
    if x2 > p1 or x1 > p2 or y1 > q2 or y2 > q1:
        result = "d"

    # 선이거나 점
    if p1 == x2:
        if q1 == y2 or q2 == y1:
            result = "c"
        else:
            result = "b"
    if p2 == x1:
        if q2 == y1 or q1 == y2:
            result = "c"
        else:
            result = "b"
    if q1 == y2:
        if p1 == x2 or p2 == x1:
            result = "c"
        else:
            result = "b"
    if q2 == y1:
        if p2 == x1 or p1 == x2:
            result = "c"
        else:
            result = "b"
    print(result)



