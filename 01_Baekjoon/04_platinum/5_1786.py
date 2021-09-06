import sys

total_words = sys.stdin.readline().replace("\n", "")
part_words = sys.stdin.readline().replace("\n", "")
part_idx = [0] * len(part_words)

i = 1
j = 0
while i < len(part_words):
    if part_words[i] == part_words[j]:
        j += 1
        part_idx[i] = j
        i += 1
    else:
        while j > 0:
            j = part_idx[j-1]
            if part_words[i] == part_words[j]:
                j += 1
                part_idx[i] = j
                break
        i += 1


# 시간초과
# for i in range(1, len(part_words)):
#     # for j in range(1, i+1):
#     #     if part_words[0:j] == part_words[i-j+1:i+1]:
#     #         part_idx[i] = j
#     #         break
#
#     # for j in range(i, 0, -1):
#     #     length = 0
#     #     for length in range(j):
#     #         if part_words[0 + length] != part_words[i - j + length + 1]:
#     #             break
#     #     else:
#     #         part_idx[i] = j
#     #         break
#
#     j = 0
#     if j > 0:
#         j = part_idx[j-1]   # 이미 저장해둔 값 활용

t_idx = 0
p_idx = 0
ans = []
while t_idx < len(total_words):
    if p_idx == len(part_words):
        ans.append(t_idx - p_idx + 1)
        p_idx = part_idx[p_idx - 1]

    # print("pattern : {}[{}], word : {}[{}]".format(part_words[p_idx], p_idx, total_words[t_idx], t_idx))
    if total_words[t_idx] == part_words[p_idx]:
        t_idx += 1
        p_idx += 1
    else:
        if p_idx == 0:
            t_idx += 1
        else:
            p_idx = part_idx[p_idx - 1]

# 마지막으로 한번 더 검사
if p_idx == len(part_words):
    ans.append(t_idx - p_idx + 1)

print(len(ans))
print(*ans)
