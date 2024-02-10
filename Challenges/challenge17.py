def divisibleSumPairs(n: int, k: int, ar: list[int]) -> int:
    number_of_pairs = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                number_of_pairs += 1

    return number_of_pairs


if __name__ == "__main__":
    first_multiple_input = input().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
