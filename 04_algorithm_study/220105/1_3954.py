# Brainf**k 인터프리터

mod = 2 ** 8
for tc in range(int(input())):
    memory_size, code_size, input_size = map(int, input().split())
    match = {}
    cmd_arr = input()
    input_arr = input()
    stack = []
    for idx, cmd in enumerate(cmd_arr):
        if cmd == '[':
            stack.append(idx)
        elif cmd == ']':
            match[stack[-1]] = idx
            match[idx] = stack[-1]
            stack.pop()
    memory_arr = [0] * memory_size
    input_idx = 0
    pointer = 0
    stack = []
    loop_cnt = 0
    cmd_idx = 0
    ans = True
    while cmd_idx < code_size:
        if loop_cnt > 100000000:
            ans = False
            break
        if cmd_arr[cmd_idx] == '-':
            memory_arr[pointer] = (memory_arr[pointer] - 1) % mod
        elif cmd_arr[cmd_idx] == '+':
            memory_arr[pointer] = (memory_arr[pointer] + 1) % mod
        elif cmd_arr[cmd_idx] == '<':
            pointer = (pointer - 1) % memory_size
        elif cmd_arr[cmd_idx] == '>':
            pointer = (pointer + 1) % memory_size
        elif cmd_arr[cmd_idx] == '[':
            if memory_arr[pointer] == 0:
                cmd_idx = match[cmd_idx]
            else:
                stack.append([cmd_idx, 0])
        elif cmd_arr[cmd_idx] == ']':
            if memory_arr[pointer] != 0:
                stack[-1][1] += 1
                cmd_idx = match[cmd_idx]
            else:
                stack.pop()
        elif cmd_arr[cmd_idx] == ',':
            if input_idx == input_size:
                memory_arr[pointer] = 255
            else:
                memory_arr[pointer] = ord(input_arr[input_idx])
                input_idx += 1

        cmd_idx += 1
        loop_cnt += 1
    if not ans:
        st = 0
        for s in stack:
            if s[1] > 0:
                st = s[0]
                break
        print(f'Loops {st} {match[st]}')
    else:
        print('Terminates')


# 4
# 10 4 3
# +-.,
# qwe
# 1000 5 1
# +[+-]
# a
# 100 74 4
# ,+++++[-[]<]>[-<+++++++>]<[->+>+>+>+<<<<]>+++>--->++++++++++>---<<<.>.>.>.
# xxyz
# 9999 52 14
# +++++[>+++++++++<-],+[-[>--.++>+<<-]>+.->[<.>-]<<,+]
# this_is_a_test