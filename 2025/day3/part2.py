def max_joltage(n: int) -> int:
    ans = 0
    with open("2025/day3/example.txt", "r") as f:
        for line in f:
            line = line.strip()
            battery = [line[0]]
            for i in range(1, len(line)):
                while len(line) - i > n - len(battery) and len(battery) > 0 and battery[-1] < line[i]:
                    battery.pop()
                if len(battery) < n:
                    battery.append(line[i])

            print(battery)
            sums = sum(10 ** (11 - i) * int(num) for i, num in enumerate(battery))
            ans += sums

    return ans


def main():
    print(max_joltage(2))
    print(max_joltage(12))

if __name__ == "__main__":
    main()
