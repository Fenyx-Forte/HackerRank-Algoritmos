def countApplesAndOranges(
    s: int, t: int, a: int, b: int, apples: list[int], oranges: list[int]
) -> None:
    apples_sam = 0
    oranges_sam = 0

    for apple in apples:
        point = a + apple
        if (point >= s) and (point <= t):
            apples_sam += 1

    for orange in oranges:
        point = b + orange
        if (point >= s) and (point <= t):
            oranges_sam += 1

    print(apples_sam)
    print(oranges_sam)


if __name__ == "__main__":
    first_multiple_input = input().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().split()))

    oranges = list(map(int, input().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
