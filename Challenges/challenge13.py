def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    # x1 + v1t = x2 + v2t
    # t(v1 - v2) = x2 - x1
    # t = (x2 - x1) / (v1 - v2)
    # x2 > x1 (CONSTRAINT)
    result = ""
    if v1 > v2:
        jumps = (x2 - x1) / (v1 - v2)
        if jumps.is_integer():
            result = "YES"

        else:
            result = "NO"

    else:
        result = "NO"

    return result


def main() -> None:
    first_multiple_input = input().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)


if __name__ == "__main__":
    main()
