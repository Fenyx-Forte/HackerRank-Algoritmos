# Counting valleys


def countingValleys(num_steps: int, steps: str) -> int:
    h = 0
    valleys = 0
    enter_valey = False

    for step in steps:
        if step == "U":
            h += 1

            if (h >= 0) and (enter_valey is True):
                enter_valey = False

        else:
            h -= 1

            if (h < 0) and (enter_valey is False):
                enter_valey = True
                valleys += 1

    return valleys


if __name__ == "__main__":
    num_steps = int(input())

    steps = input()

    result = countingValleys(num_steps, steps)

    print(result)
