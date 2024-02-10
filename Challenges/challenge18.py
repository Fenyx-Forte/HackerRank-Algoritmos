from collections import Counter


def migratoryBirds(arr: list[int]) -> int:
    dict_counter = Counter(sorted(arr))

    lowest_id_most_frequently = dict_counter.most_common(1)[0][0]

    return lowest_id_most_frequently


def main() -> None:
    arr_count = int(input().strip())

    arr = list(map(int, input().split()))

    result = migratoryBirds(arr)

    print(result)


if __name__ == "__main__":
    main()
