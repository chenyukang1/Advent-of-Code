

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


def main():
    print(calculate())

if __name__ == "__main__":
    main()
