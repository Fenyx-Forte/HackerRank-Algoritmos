def birthdayCakeCandles(candles: list[int]) -> int:
    result = candles.count(max(candles))

    return result


def main() -> None:
    candles_count = int(input().strip())

    candles = list(map(int, input().split()))

    result = birthdayCakeCandles(candles)

    print(result)


if __name__ == "__main__":
    main()
