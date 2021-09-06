# 방배정
import math
student_len, max_len = map(int, input().split())
room_cnt = 0
student = [[0] * 2 for _ in range(6)]

for _ in range(student_len):
    gender, grade = map(int, input().split())
    student[grade-1][gender] += 1

# 학년별, 성별 이차원 리스트를 돌며 최대 인원 갯수만큼 나눈 수를 올림한 뒤 더해준다.
for grade in range(6):
    for gender in range(2):
        room_cnt += math.ceil(student[grade][gender] / max_len)
print(room_cnt)