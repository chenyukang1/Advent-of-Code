def bsf(root, buttons) -> int:
    if all(not item for item in root):
        return 0
    queue = [root]
    visited = [tuple(root)]
    depth = 0
    while len(queue) > 0:
        size = len(queue)
        depth += 1
        for _ in range(size):
            lights = queue.pop(0)
            for button in buttons:
                copy = lights[:]
                for idx in button:
                    copy[idx] = not copy[idx]
                if all(not item for item in copy):
                    return depth

                copy_tupe = tuple(copy)
                if copy_tupe not in visited:
                    visited.append(copy_tupe)
                    queue.append(copy)

    return depth

sum = 0
for line in open('2025/day10/input.txt', 'r').read().splitlines():
    i, j = line.find(']'), line.find('{')
    lights = [True if item == '#' else False for item in line[line.find('[') + 1: i]]
    mid = line[i + 2 : j - 1].strip("()").split(") (")
    buttons = [tuple(map(int, item.split(','))) for item in mid]
    sum += bsf(lights, buttons=buttons)

print(sum)
