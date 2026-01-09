
def split_times() -> int:
    p1 = 0
    with open('2025/day7/example.txt', 'r') as f:
          lines = f.readlines()

    beams = set()
    beams.add(lines[0].find('S'))
    for i in range(2, len(lines), 2):
        line = lines[i].strip()
        for s, n in enumerate(line):
            if n == '^' and s in beams:
                p1 += 1
                beams.remove(s)
                if s-1 >= 0:
                    beams.add(s-1)
                if s+1 < len(line):
                    beams.add(s+1)
    return p1


def main():
    print(split_times())

if __name__ == "__main__":
    main()
