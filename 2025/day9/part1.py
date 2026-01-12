grid = [
    tuple(line.strip().split(","))
    for line in open("2025/day9/input.txt", "r").read().splitlines()
]
n = len(grid)
print(max([(abs(int(grid[i][0]) - int(grid[j][0]))+1) * abs(int(grid[i][1]) - int(grid[j][1])+1) for i in range(n-1) for j in range(1, n)]))
