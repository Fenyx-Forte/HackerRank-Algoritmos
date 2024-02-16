# Day of the Programmer
def dayOfProgrammer(year: int) -> str:
    if 1700 <= year < 1918:
        if year % 4 == 0:
            return f"12.09.{str(year)}"
        else:
            return f"13.09.{str(year)}"
    elif 1918 < year <= 2700:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return f"12.09.{str(year)}"
        else:
            return f"13.09.{str(year)}"
    else:
        return f"26.09.{str(year)}"


def main() -> None:
    year = int(input())

    result = dayOfProgrammer(year)

    print(result)


if __name__ == "__main__":
    main()
