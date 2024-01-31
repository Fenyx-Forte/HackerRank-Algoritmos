def staircase(n: int) -> None:
    for i in range(n):
        string = ("#" * (i + 1)).rjust(n)
        print(string)


def main() -> None:
    n = int(input().strip())

    staircase(n)


if __name__ == "__main__":
    main()
