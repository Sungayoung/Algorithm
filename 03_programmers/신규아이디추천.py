def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for word in new_id:
        if not word.isalnum() and word not in ['-', '_', '.']:
            continue
        answer += word
    print(answer)
    new_answer = answer[:]

    answer = ''
    stack = []
    for word in new_answer:
        if word.isalnum():
            stack = []
            answer += word
        else:
            if word == '.' and not stack:
                stack.append('.')
                answer += word
            elif word in ['-', '_']:
                stack = []
                answer += word
    print(answer)
    answer = answer.strip('. ')

    if len(answer) == 0:
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('. ')

    while len(answer) <= 2:
        answer += answer[-1]
    return answer

print(solution("v...............v"))
