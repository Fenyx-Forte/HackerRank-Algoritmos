def catAndMouse(x: int, y: int, z: int) -> str:
    result = ""

    dist_cat_a = abs(x - z)
    dist_cat_b = abs(y - z)

    if dist_cat_a == dist_cat_b:
        result = "Mouse C"

    elif dist_cat_a > dist_cat_b:
        result = "Cat B"

    else:
        result = "Cat A"

    return result


def main() -> None:
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)


if __name__ == "__main__":
    main()
