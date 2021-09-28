def solution(board, skill):
    answer = 0
    for i in range(len(skill)):
        # 공격
        if skill[i][0] == 1:
            for r in range(skill[i][1], skill[i][3]+1):
                for c in range(skill[i][2], skill[i][4]+1):
                    board[r][c] -= skill[i][5]

        # 회복
        else:
            for r in range(skill[i][1], skill[i][3]+1):
                for c in range(skill[i][2], skill[i][4]+1):
                    board[r][c] += skill[i][5]

    print(board)
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] > 0:
                answer += 1
    return answer

print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))