def secret_entrance_password() -> int:
    pointer = 50
    ans = 0
    with open('2025/day1/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            num = int(line[1:])
            ans += num // 100

            if line[0] == 'R':
                pointer += num % 100
                if pointer >= 100:
                    ans += 1
                    pointer -= 100
            elif line[0] == 'L':
                zero = pointer == 0
                pointer -= num % 100
                if pointer < 0:
                    pointer += 100
                    if not zero:
                        ans += 1
                elif pointer == 0:
                    ans += 1
                # positive = pointer > 0
                # pointer -= num % 100
                # if pointer <= 0:
                #     pointer += 100
                #     if positive:
                #         ans += 1
                # if pointer == 100:
                #     pointer = 0

    return ans


def main():
    print(secret_entrance_password())

if __name__ == "__main__":
    main()
