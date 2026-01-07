def secret_entrance_password() -> int:
    pointer = 50
    ans = 0
    with open('2025/day1/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            num = int(line[1:])
            if line[0] == 'R':
                pointer += num % 100
                if pointer >= 100:
                    pointer -= 100
            elif line[0] == 'L':
                pointer -= num % 100
                if pointer < 0:
                    pointer += 100

            if pointer == 0:
                ans += 1

    return ans


def main():
    print(secret_entrance_password())

if __name__ == "__main__":
    main()
