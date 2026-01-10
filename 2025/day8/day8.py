import math


# 构建邻接矩阵搜索，O(n^3)
def three_largest_circuit_sizes() -> int:
    boxes = [
        tuple([int(i) for i in line.strip().split(",")])
        for line in open("2025/day8/input.txt", "r").read().splitlines()
    ]
    n = len(boxes)
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            grid[i][j] = (
                (boxes[j][0] - boxes[i][0]) ** 2
                + (boxes[j][1] - boxes[i][1]) ** 2
                + (boxes[j][2] - boxes[i][2]) ** 2
            )

    visited = [[False for _ in range(n)] for _ in range(n)]
    circuits = []
    for _ in range(1001):
        min = float("inf")
        min_tuple = (0, 0)
        for i in range(n):
            for j in range(i + 1, n):
                if visited[i][j]:
                    continue
                if grid[i][j] < min:
                    min = grid[i][j]
                    min_tuple = (i, j)
        visited[min_tuple[0]][min_tuple[1]] = True

        found = False
        for circuit in circuits:
            if min_tuple[0] in circuit and min_tuple[1] in circuit:
                found = True
                break
            if min_tuple[0] in circuit:
                found = True
                circuit.append(min_tuple[1])
                break
            elif min_tuple[1] in circuit:
                found = True
                circuit.append(min_tuple[0])
                break
        if found is False:
            circuits.append([min_tuple[0], min_tuple[1]])

    print(circuits)

    lens = sorted([len(circuit) for circuit in circuits])
    return math.prod(len for i, len in enumerate(reversed(lens)) if i < 3)


def three_largest_circuit_sizes_v2(connect_timtes) -> int:
    grid = [
        tuple(int(i) for i in line.strip().split(","))
        for line in open("2025/day8/input.txt", "r").read().splitlines()
    ]
    n = len(grid)

    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            distances.append((i, j, math.dist(grid[i], grid[j])))

    distances.sort(key=lambda x: x[2])

    # dict模拟并查集
    parent = {i: i for i in range(n)}
    size = {i: 1 for i in range(n)}
    union_count = 0

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i, root_j = find(i), find(j)
        if root_i == root_j:
            return False
        parent[root_i] = root_j
        size[root_j] += size[root_i]
        return True

    if connect_timtes:
        for i in range(connect_timtes):
            union(distances[i][0], distances[i][1])
        top_three = sorted([size[i] for i in range(n) if parent[i] == i], reverse=True)[:3]

        return math.prod(top_three)
    else:
        for i, j, dist in distances:
            if union(i, j):
                union_count += 1
            if union_count == n - 1:
                last_pair = (i, j)
                break

        print(parent)
        return grid[last_pair[0]][0] * grid[last_pair[1]][0]


if __name__ == "__main__":
    # print(three_largest_circuit_sizes())
    p1, p2 = three_largest_circuit_sizes_v2(1000), three_largest_circuit_sizes_v2(None)
    print(f"p1: {p1}")
    print(f"p1: {p2}")
