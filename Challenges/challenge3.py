def compareTriplets(alice: list[int], bob: list[int]) -> list[int]:
    alice_points = 0
    bob_points = 0
    num_categories = 3
    for i in range(num_categories):
        if alice[i] > bob[i]:
            alice_points += 1
        elif alice[i] < bob[i]:
            bob_points += 1

    return [alice_points, bob_points]


def main() -> None:
    alice = [*map(int, input().split())]

    bob = [*map(int, input().split())]

    result = compareTriplets(alice, bob)

    print(*result)


if __name__ == "__main__":
    main()
