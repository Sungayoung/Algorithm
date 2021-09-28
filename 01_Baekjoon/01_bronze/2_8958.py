# OX퀴즈

for _ in range(int(input())):
    quiz = input()
    plus = 0
    result = 0
    for q in quiz:
        if q == 'O':
            plus += 1
            result += plus
        else:
            plus = 0
    print(result)
