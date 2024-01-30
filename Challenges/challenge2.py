def simpleArraySum(ar: list[int]) -> int:
    return sum(ar)


def main() -> None:
    n = int(input())

    array = [*map(int, input().split())]

    result = simpleArraySum(array)

    print(result)


if __name__ == "__main__":
    main()
