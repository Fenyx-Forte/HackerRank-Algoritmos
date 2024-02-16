# Drawing Book
from math import ceil, floor


def page_count_begin(n: int, p: int) -> int:
    return ceil((p - 1) / 2)


def page_count_end(n: int, p: int) -> int:
    if n % 2 == 0:
        return ceil((n - p) / 2)

    return floor((n - p) / 2)


def pageCount(n: int, p: int) -> int:
    begin = page_count_begin(n, p)
    end = page_count_end(n, p)
    result = min(begin, end)

    return result


def main() -> None:
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)


if __name__ == "__main__":
    main()
