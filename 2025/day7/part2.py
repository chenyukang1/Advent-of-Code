

# 回溯，时间复杂度O(2^n)
def time_lines() -> int:
    with open("2025/day7/input.txt", "r") as f:
        lines = f.readlines()
    n = len(lines)

    def get_time_lines(i: int, beams) -> int:
        if i >= n:
            return 1

        hits = [j for j in beams if lines[i][j] == "^"]
        if not hits:
            return get_time_lines(i + 2, beams)

        possible_beams = []
        num_hits = len(hits)

        def get_all_possible_beams(i, path):
            if len(path) == num_hits:
                possible_beams.append(path[:])
            for j in range(i, num_hits):
                for dir in [-1, 1]:
                    path.append(hits[j] + dir)
                    get_all_possible_beams(j + 1, path)
                    path.pop()

        get_all_possible_beams(0, [])
        print(possible_beams)

        return sum([get_time_lines(i + 2, beams) for beams in possible_beams])

    beams = set()
    beams.add(lines[0].find('S'))
    return get_time_lines(2, beams)


# 记忆化搜索，下方的障碍分布是死的，那么从这一刻起，你往后演化出的所有可能性就已经被地图决定了
def time_lines_v2() -> int:
    grid = [list(line) for line in open('2025/day7/input.txt', 'r').read().splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    mem = {}

    def get_time_lines(row: int, col: int) -> int:
        if row >= rows or col < 0 or col >= cols:
            return 1

        if (row, col) in mem:
            return mem[(row, col)]

        res = 0
        if grid[row][col] == '.':
            return get_time_lines(row+1, col)
        else:
            res += get_time_lines(row+1, col-1)
            res += get_time_lines(row+1, col+1)
        mem[(row, col)] = res

        return res

    return get_time_lines(0, grid[0].index('S'))


if __name__ == "__main__":
    print(time_lines_v2())
