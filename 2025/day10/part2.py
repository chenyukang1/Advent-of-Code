from collections import deque
import multiprocessing
import os
import z3


# bsf遍历所有可能情况，too slow
def fewest_button_presses() -> int:
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

    return sum


# ---------------------------------v2剪枝版本---------------------------------
def get_combinations(matching_buttons, maxima, target):
    # for buttion in matching_buttons press limit maxima[i], sum(idx) == target
    ans = []
    num_buttons = len(matching_buttons)

    def back_track(start: int, sum, path):
        if start == num_buttons:
            if sum == target:
                ans.append(path[:])
            return

        for count in range(min(maxima[start], target - sum) + 1):
            path.append(count)
            back_track(start + 1, sum + count, path)
            path.pop()

    back_track(0, 0, [])
    return ans

def dsf(available_buttons: list, joltage) :
    if all(v == 0 for v in joltage):
        return 0
    # 最窄约束位
    best_idx = -1
    min_button_count = float('inf')
    for i, v in enumerate(joltage):
        if v > 0:
            count = sum(1 for b in available_buttons if i in b)
            if count < min_button_count:
                min_button_count = count
                best_idx = i
            elif count == min_button_count:
                # 第二优先级：值越大越优先
                if best_idx == -1 or v > joltage[best_idx]:
                    best_idx = i

    matching_buttons = [b for b in available_buttons if best_idx in b]
    remaining_buttons = [b for b in available_buttons if b not in matching_buttons]

    maxima = []
    for b in matching_buttons:
        limit = min(joltage[i] for i in b)
        maxima.append(limit)

    min_total_presses = float('inf')
    combinations = get_combinations(matching_buttons, maxima, joltage[best_idx])
    for combination in combinations:
        new_joltage = list(joltage)
        possible = True
        total_presses = sum(combination)

        for idx, count in enumerate(combination):
            if count == 0:
                continue
            for button in matching_buttons[idx]:
                if new_joltage[button] >= count:
                    new_joltage[button] -= count
                else:
                    possible = False
                    break
            if not possible:
                break

        if possible:
            res = dsf(remaining_buttons, tuple(new_joltage))
            if res != float('inf'):
                min_total_presses = min(min_total_presses, total_presses + res)

    return min_total_presses

def dsf_task(tasks):
    local_sum = 0
    for task in tasks:
        local_sum += dsf(task[0], task[1])
    return local_sum

def fewest_button_presses_v2() -> int:

    inputs = []
    for line in open('2025/day10/input.txt', 'r').read().splitlines():
        i, j = line.find(']'), line.find('{')
        mid = line[i + 2 : j - 1].strip("()").split(") (")
        buttons = [tuple(map(int, item.split(','))) for item in mid]
        target = tuple(int(item) for item in line[j + 1 : -1].split(','))
        max_target = max(target)
        inputs.append((buttons, target, max_target))
    inputs.sort(key=lambda x: x[2])

    n = len(inputs)
    if n > 3:
        tasks = [(input[0], input[1]) for input in inputs]
        cores = os.cpu_count()
        cores = cores if cores else 4
        task_groups = [[] for _ in range(cores)]
        for i, task in enumerate(tasks):
            task_groups[i % cores].append(task)

        with multiprocessing.Pool(processes=cores) as pool:
            group_results = pool.map(dsf_task, task_groups)

        return sum(group_results)
    else:
        return sum(dsf(input[0], input[1]) for input in inputs)


def fewest_button_presses_v3() -> int:
    p2 = 0
    for line in open('2025/day10/input.txt', 'r').read().splitlines():
        i, j = line.find(']'), line.find('{')
        mid = line[i + 2 : j - 1].strip("()").split(") (")
        buttons = [tuple(map(int, item.split(','))) for item in mid]
        joltage_ns = [int(x) for x in line[j + 1 : -1].split(',')]
        B = []
        NS = []
        for button in buttons:
            ns = [idx for idx in button]
            button_n = sum(2**x for x in ns)
            B.append(button_n)
            NS.append(ns)
        V = []
        for i in range(len(buttons)):
            V.append(z3.Int(f'B{i}'))
        EQ = []
        for i in range(len(joltage_ns)):
            terms = []
            for j in range(len(buttons)):
                if i in NS[j]:
                    terms.append(V[j])
            eq = (sum(terms) == joltage_ns[i])
            EQ.append(eq)
        o = z3.Optimize()
        o.minimize(sum(V))
        for eq in EQ:
            o.add(eq)
        for v in V:
            o.add(v >= 0)
        assert o.check()
        M = o.model()
        for d in M.decls():
            #print(d.name(), M[d])
            p2 += M[d].as_long()
    return p2

if __name__ == "__main__":
    # ans = fewest_button_presses_v2()
    # print(ans)
    print(fewest_button_presses_v3())
