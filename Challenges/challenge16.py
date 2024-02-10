def birthday(s: list[int], d: int, m: int) -> int:
    total = 0
    len_s = len(s)

    for i in range(len_s - m + 1):
        if sum(s[i : i + m]) == d:
            total += 1

    return total


def main() -> None:
    n = int(input().strip())

    s = list(map(int, input().split()))

    first_multiple_input = input().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)


if __name__ == "__main__":
    main()
