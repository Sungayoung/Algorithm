def solution(n, computers):
    answer = 0

    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        stack = [i]
        visited[i] = True
        while stack:
            cur = stack.pop()
            for j in range(n):
                if i != j and not visited[j] and computers[cur][j]:
                    visited[j] = True
                    stack.append(j)
        answer += 1
    return answer

print()