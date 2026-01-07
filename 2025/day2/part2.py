from typing import List


def invalid_ids() -> int:
    ans = 0
    with open('2025/day2/input.txt', 'r') as f:
        line = f.readline().strip()
        for symbol in line.split(','):
            sf = symbol.split('-')
            start = int(sf[0])
            end = int(sf[1])
            for i in range(start, end + 1):
                target = str(i)
                next = build_next(target)
                n = len(target)
                L = next[n - 1]
                if L > 0 and n % (n - L) == 0:
                    ans += i

    return ans


def build_next(target: str) -> List[int]:
    next = [0]
    j = 0
    for i in range(1, len(target)):
        while j > 0 and target[j] != target[i]:
            j = next[j - 1]
        if target[j] == target[i]:
           j += 1
        next.append(j)

    return next


def main():
    print(invalid_ids())

if __name__ == "__main__":
    main()
