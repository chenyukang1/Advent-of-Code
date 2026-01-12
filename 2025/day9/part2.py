grid = [tuple(int(x) for x in line.split(',')) for line in open('2025/day9/input.txt').read().splitlines()]
n = len(grid)


def do_lines_intersect(p1, p2, q1, q2) -> bool:
    """
    判断线段 (p1, p2) 和 (q1, q2) 是否相交（不包含端点接触）
    p1, p2, q1, q2 均为 [x, y] 或 (x, y) 格式
    """
    def cross_2d(v_x, v_y, w_x, w_y):
        return v_x * w_y - v_y * w_x

    # 计算向量 r = p2 - p1
    rx, ry = p2[0] - p1[0], p2[1] - p1[1]
    # 计算向量 s = q2 - q1
    sx, sy = q2[0] - q1[0], q2[1] - q1[1]

    # 计算分母 r × s
    denominator = cross_2d(rx, ry, sx, sy)

    # 计算向量 (q1 - p1)
    q1p1x, q1p1y = q1[0] - p1[0], q1[1] - p1[1]

    # 计算分子 (q1 - p1) × r
    u_numerator = cross_2d(q1p1x, q1p1y, rx, ry)

    # 情况 1: 分母为 0，说明两条线段平行或共线
    if denominator == 0:
        # 在你的逻辑中，共线或平行均视为不相交
        return False

    # 情况 2: 分母不为 0，计算参数 t 和 u
    # t = (q - p) × s / (r × s)
    # u = (q - p) × r / (r × s)
    t = cross_2d(q1p1x, q1p1y, sx, sy) / denominator
    u = u_numerator / denominator

    # 判断交点是否在两条线段的范围内 (0 <= t, u <= 1)
    if (0 <= t <= 1) and (0 <= u <= 1):
        # 你的原逻辑排除了端点接触的情况（即交点不能是 p1, p2, q1, q2）
        # 对应 t, u 为 0 或 1 的情况
        # 这里为了防止浮点数精度问题，使用一个极小的阈值 epsilon
        eps = 1e-9
        if (eps < t < 1 - eps) and (eps < u < 1 - eps):
            return True

    return False


def is_intersect(i, j, grid):
    # 矩形的四个顶点
    p1 = grid[i] # (x1, y1)
    p2 = grid[j] # (x2, y2)
    p3 = (p1[0], p2[1]) # (x1, y2)
    p4 = (p2[0], p1[1]) # (x2, y1)

    # 需要检查的所有矩形线段（4条边 + 2条对角线）
    rect_segments = [
        (p1, p3), (p3, p2), (p2, p4), (p4, p1), # 四条边
        (p1, p2), (p3, p4)                      # 对角线
    ]

    for k in range(n):
        # 多边形的边
        edge_start = grid[k]
        edge_end = grid[(k + 1) % n]
        for r_start, r_end in rect_segments:
            if do_lines_intersect(r_start, r_end, edge_start, edge_end):
                return True

    return False


max_area = 0
for i in range(n-1):
    for j in range (i+1, n):
        if is_intersect(i, j, grid):
            print(f'{grid[i]} {grid[j]} intersect!')
        else:
            area = (abs(grid[i][0] - grid[j][0]) + 1) * (abs(grid[i][1] - grid[j][1]) + 1)
            print(f'found {grid[i]} {grid[j]} {area}')
            max_area = max(max_area, area)

print(max_area)
