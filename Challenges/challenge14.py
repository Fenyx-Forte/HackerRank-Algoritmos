def getTotalX(a: list[int], b: list[int]) -> int:
    total = 0

    max_a = max(a)
    min_b = min(b)

    for i in range(max_a, min_b + 1):
        i_satisfy = True
        for num in a:
            if i % num != 0:
                i_satisfy = False
                break

        if i_satisfy:
            for number in b:
                if number % i != 0:
                    i_satisfy = False
                    break

        if i_satisfy:
            total += 1

    return total


def main() -> None:
    first_multiple_input = input().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)


if __name__ == "__main__":
    main()
