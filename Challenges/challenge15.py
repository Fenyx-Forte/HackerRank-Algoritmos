def breakingRecords(scores: list[int]) -> list[int]:
    min_break_records = 0
    max_break_records = 0

    min_record = scores[0]
    max_record = scores[0]

    for score in scores:
        if score > max_record:
            max_break_records += 1
            max_record = score

        if score < min_record:
            min_break_records += 1
            min_record = score

    return [max_break_records, min_break_records]


def main() -> None:
    n = int(input().strip())

    scores = list(map(int, input().split()))

    result = breakingRecords(scores)
    print(*result)


if __name__ == "__main__":
    main()
