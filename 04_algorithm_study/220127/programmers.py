# 파괴되지 않은 건물

# 누적합 이용

def solution(board, skill):
    height = len(board)
    width = len(board[0])

    square = [[0] * (width + 1) for _ in range(height + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree

        square[r1][c1] += degree
        square[r1][c2 + 1] += -degree
        square[r2 + 1][c1] += -degree
        square[r2 + 1][c2 + 1] += degree

    for i in range(height + 1):
        for j in range(width):
            square[i][j + 1] += square[i][j]

    for j in range(width + 1):
        for i in range(height):
            square[i + 1][j] += square[i][j]

    answer = 0
    for r in range(height):
        for c in range(width):
            board[r][c] += square[r][c]
            if board[r][c] > 0:
                answer += 1
    return answer


def main():
    solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]])

if __name__ == '__main__':
    main()