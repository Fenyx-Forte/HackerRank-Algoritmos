def aVeryBigSum(ar: list[int]) -> int:
    return sum(ar)


def main() -> None:
    ar_count = int(input().strip())

    ar = list(map(int, input().split()))

    result = aVeryBigSum(ar)

    print(result)


if __name__ == "__main__":
    main()
