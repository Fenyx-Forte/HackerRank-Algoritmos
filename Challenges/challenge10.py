def formate_string_24hr(hours: int, minutes: str, seconds: str) -> str:
    string = f"{hours:0>2}:{minutes}:{seconds}"
    return string


def timeConversion(string: str) -> str:
    split_string = string.split(":")
    hours = int(split_string[0])
    minutes = split_string[1]
    sec = split_string[2][:2]
    am_pm_format = split_string[2][2:]

    result = ""
    if am_pm_format == "PM":
        if hours >= 12:
            result = string[:-2]
        else:
            result = formate_string_24hr((hours + 12), minutes, sec)

    else:
        if hours >= 12:
            result = formate_string_24hr((hours - 12), minutes, sec)
        else:
            result = string[:-2]

    return result


def main() -> None:
    string = input()

    result = timeConversion(string)

    print(result)


if __name__ == "__main__":
    main()
