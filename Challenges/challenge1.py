def solveMeFirst(a: int, b: int) -> int:
    return a + b


def main() -> None:
    num1 = int(input())
    num2 = int(input())
    res = solveMeFirst(num1, num2)
    print(res)


if __name__ == "__main__":
    main()
