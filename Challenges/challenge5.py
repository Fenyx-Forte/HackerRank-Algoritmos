def diagonalDifference(arr: list[list[int]]) -> int:
    sum_left_to_right_diagonal = 0
    sum_right_to_left_diagonal = 0
    len_arr = len(arr)

    for i in range(len_arr):
        sum_left_to_right_diagonal += arr[i][i]
        sum_right_to_left_diagonal += arr[i][len_arr - i - 1]

    return abs(sum_left_to_right_diagonal - sum_right_to_left_diagonal)


if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
