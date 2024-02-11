def bonAppetit(bill: list[int], k: int, b: int) -> None:
    total = sum(bill) - bill[k]

    anna = total // 2

    if anna == b:
        print("Bon Appetit")

    else:
        print(b - anna)


def main() -> None:
    first_multiple_input = input().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().split()))

    b = int(input())

    bonAppetit(bill, k, b)


if __name__ == "__main__":
    main()
