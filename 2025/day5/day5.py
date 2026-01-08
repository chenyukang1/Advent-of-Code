def fresh_ingredient_ids(part1: bool) -> int:
    ans = 0
    ranges = []
    ids = []
    with open('2025/day5/input.txt', 'r') as f:
        before = True
        for line in f:
            if not len(line.strip()):
                before = False
                continue
            if before:
                ranges.append(line.strip())
            else:
                ids.append(line.strip())

    ranges = merge_ranges(ranges)

    if part1:
        for id in ids:
            for r in ranges:
                s = r.split('-')
                if int(id) >= int(s[0]) and int(id) <= int(s[1]):
                    ans += 1
                    break
    else:
       for r in ranges:
           s = r.split('-')
           ans += int(s[1]) - int(s[0]) + 1

    return ans


# 合并有序数组
def merge_ranges(ranges: list) -> list:
    new_ranges = []
    ranges.sort(key=lambda x: int(x.split('-')[0]))
    first_s = ranges[0].split('-')
    cur_left, cur_right = int(first_s[0]), int(first_s[1])

    for i in range(1, len(ranges)):
        s = ranges[i].split('-')
        next_left, next_right = int(s[0]), int(s[1])
        if next_left <= cur_right:
            cur_right = max(cur_right, next_right)
        else:
            new_ranges.append(f'{cur_left}-{cur_right}')
            cur_left, cur_right = next_left, next_right
    new_ranges.append(f'{cur_left}-{cur_right}')

    return new_ranges


def main():
    print(fresh_ingredient_ids(True)) # part1
    print(fresh_ingredient_ids(False)) # part2

if __name__ == "__main__":
    main()
