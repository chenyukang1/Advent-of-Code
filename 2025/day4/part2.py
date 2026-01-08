def rolls_of_paper() -> int:
    rolls = []
    with open('2025/day4/input.txt', 'r') as f:
        for line in f:
            rolls.append(list(line.strip()))

    def remove_papers() -> int:
        removed = 0
        dirs = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        rows, cols = len(rolls), len(rolls[0])
        for i, row in enumerate(rolls):
            for j, letter in enumerate(row):
                if letter != '@':
                    continue
                count = 0
                for dir in dirs:
                    newY = i + dir[0]
                    newX = j + dir[1]
                    if (newY >= 0 and newY < rows and newX >=0 and newX < cols
                        and rolls[newY][newX] == '@'):
                        count += 1
                if count < 4:
                    print(f'found at {i} {j}')
                    rolls[i][j] = '.'
                    removed += 1
        if removed > 0:
            return remove_papers() + removed
        return 0

    return remove_papers()


def main():
    print(rolls_of_paper())

if __name__ == "__main__":
    main()
