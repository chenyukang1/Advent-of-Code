from collections import deque


def bsf(buttons, target):
    root = tuple([0 for _ in target])
    if root == target:
        return 0
    queue = deque([root])
    visited = {tuple(root)}
    depth = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            cur = list(queue.popleft())
            for button in buttons:
                copy = cur[:]
                for idx in button:
                    if copy[idx] >= target[idx]:
                        break
                    copy[idx] += 1
                else:
                    state = tuple(copy)
                    if state == target:
                        return depth + 1
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
        depth += 1

    return -1

sum = 0
for line in open('2025/day10/input.txt', 'r').read().splitlines():
    i, j = line.find(']'), line.find('{')
    mid = line[i + 2 : j - 1].strip("()").split(") (")
    buttons = [tuple(map(int, item.split(','))) for item in mid]
    target = tuple(int(item) for item in line[j + 1 : -1].split(','))
    sum += bsf(buttons, target)

print(sum)
