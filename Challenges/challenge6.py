def plusMinus(arr: list[int]) -> None:
    positive_numbers = len([num for num in arr if num > 0])
    negative_numbers = len([num for num in arr if num < 0])
    zero_numbers = len([num for num in arr if num == 0])

    total_numbers = len(arr)

    positive_ratio = positive_numbers / total_numbers
    negative_ratio = negative_numbers / total_numbers
    zero_ratio = zero_numbers / total_numbers

    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().split()))

    plusMinus(arr)
