def seven_dwarfs(height):
    height_sum = sum(height)
    for i in range(8):
        for j in range(i + 1, 9):
            if height_sum - height[i] - height[j] == 100:
                num1, num2 = height[i], height[j]
                height.remove(num1)
                height.remove(num2)
                return height

height = []

for _ in range(9):
    height.append(int(input()))
height.sort()
print(*seven_dwarfs(height), sep="\n")