import math


def calculate() -> int:
    p1 = 0
    nums = []
    with open('2025/day6/input.txt', 'r') as f:
        for num in f.readline().strip().split():
            nums.append([num])

        for line in f.readlines():
            for i, s in enumerate(line.strip().split()):
                nums[i].append(s)

        for num in nums:
            match num[-1]:
                case '+':
                    p1 += sum(int(n) for n in num[:-1])
                case '*':
                    p1 += math.prod(int(n) for n in num[:-1])

    return p1


def calculate_v2() -> int:
    with open('2025/day6/input.txt', 'r') as f:
        columns = [int(num) for num in f.readline().split()]
        lines = f.readlines()
        signs = lines[-1].split()
        for line in lines[:-1]:
            for i in range(len(columns)):
                match signs[i]:
                    case '+':
                        columns[i] += int(line.split()[i])
                    case '*':
                        columns[i] *= int(line.split()[i])
        return sum(columns)


def main():
    print(calculate())
    print(calculate_v2())

if __name__ == "__main__":
    main()
