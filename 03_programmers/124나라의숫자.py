def solution(n):
    answer = ''
    i = 1
    prev_sum = 0
    nums = ['1', '2', '4']
    while True:
        cur_sum = 3 * (1 - 3 ** i) / -2
        # print(cur_sum)
        if prev_sum < n <= cur_sum:
            break
        i += 1
        prev_sum = cur_sum
    n -= prev_sum + 1
    n = int(n)
    while n > 0:
        remainder = n % 3
        answer += str(nums[remainder])
        n //= 3

    while len(answer) < i:
        answer += nums[n]

    return answer[::-1]


print(solution(3))
