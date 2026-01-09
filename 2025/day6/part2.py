

import math


def calculate() -> int:
    p2 = 0
    nums = []
    blanks = []
    signs = []
    with open('2025/day6/input.txt', 'r') as f:
        lines = f.readlines()
        positions = [i for i, c in enumerate(lines[-1]) if c in ('+', '*')]
        for i in range(len(positions) - 1):
            blanks.append(positions[i+1] - positions[i] - 1)
            nums.append([])
        blanks.append(len(lines[-1]) - positions[len(positions) - 1] - 1)
        nums.append([])

        for line in lines[:-1]:
            left, right = 0, blanks[0]
            for i in range(1, len(blanks)):
                nums[i-1].append(line[left:right].replace(' ', '0'))
                left = right + 1
                right = left + blanks[i]
            nums[len(nums) -1].append(line[left:right].replace(' ', '0').replace('\n', '0'))
        print(nums)

        for c in lines[-1].strip().split():
            signs.append(c)

        for j, arr in enumerate(nums):
            n = len(arr[0])
            match signs[j]:
                case '*':
                    res = 1
                    for i in range(n):
                        multi = 0
                        m = 0
                        for num in reversed(arr):
                            if num[i] != '0':
                                multi += 10 ** m * int(num[i])
                                m += 1
                        print(multi)
                        res *= multi
                    p2 += res

                case '+':
                    res = 0
                    for i in range(n):
                        add = 0
                        m = 0
                        for num in reversed(arr):
                            if num[i] != '0':
                                add += 10 ** m * int(num[i])
                                m += 1
                        print(add)
                        res += add
                    p2 += res

    return p2

def calcluate_v2() -> int:
    p2 = 0
    nums = []
    with open('2025/day6/input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines[:-1]:
            nums.append([s for s in line.strip('\n')])
        operations = [s for s in lines[-1].split()]

    cols = len(nums[0])
    rows = len(nums)
    nums_in_cols = []
    for col in range(cols - 1, -2, -1):
        if all(nums[row][col] == ' ' for row in range(0, rows)) or col == -1:
            operation = operations.pop()
            print(nums_in_cols)
            if operation == '+':
                p2 += sum(nums_in_cols)
            if operation == '*':
                p2 += math.prod(nums_in_cols)
            nums_in_cols = []

        else:
            m = 0
            num = 0
            for row in range(rows - 1, -1, -1):
                if nums[row][col] != ' ':
                    num += 10 ** m * int(nums[row][col])
                    m += 1
            nums_in_cols.append(num)

    return p2


def main():
    # print(calculate())
    print(calcluate_v2())

if __name__ == "__main__":
    main()
