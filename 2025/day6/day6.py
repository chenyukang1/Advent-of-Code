
import math


def calculate() -> tuple[int, int]:
    p1 = 0
    p2 = 0
    nums = []
    with open('2025/day6/input.txt', 'r') as f:
        for num in f.readline().strip().split():
            if num:
                nums.append([num])

        for line in f.readlines():
            for i, s in enumerate(line.strip().split()):
                if s:
                    nums[i].append(s)

        for num in nums:
            match num[-1]:
                case '+':
                    p1 += sum(int(n) for n in num[:-1])
                case '*':
                    p1 += math.prod(int(n) for n in num[:-1])

        for num in nums:
            max_l = len(num[0])
            for i in range(1, len(num)):
                max_l = max(max_l, len(num[i]))
            for n in num:
                for i in range(max_l):
                    if not n[i]:
                        n.append('0')
            for i in range(max_l):
                # todo
                pass

    return p1, p2


def main():
    print(calculate())

if __name__ == "__main__":
    main()
