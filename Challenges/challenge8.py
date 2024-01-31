def miniMaxSum(arr: list[int]) -> None:
    total_sum = sum(arr)

    mini_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)

    print(mini_sum, max_sum)


def main():
    arr = list(map(int, input().split()))

    miniMaxSum(arr)


if __name__ == "__main__":
    main()
