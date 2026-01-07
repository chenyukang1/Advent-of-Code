def invalid_ids() -> int:
    ans = 0
    with open('2025/day2/input.txt', 'r') as f:
        line = f.readline().strip()
        for symbol in line.split(','):
            sf = symbol.split('-')
            start = int(sf[0])
            end = int(sf[1])
            for i in range(start, end + 1):
                if (twice_repeated(str(i))):
                    ans += i

    return ans


def twice_repeated(num: str) -> bool:
    if len(num) % 2 == 1:
        return False
    i ,j = 0, len(num) // 2
    while i < len(num) // 2:
        if num[i] != num[j]:
            return False
        i += 1
        j += 1

    return True


def main():
    print(invalid_ids())


if __name__ == "__main__":
    main()
