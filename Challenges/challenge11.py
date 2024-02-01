def gradingStudents(grades: list[int]) -> list[int]:
    rounded_grades = []

    for grade in grades:
        next_mul_5 = grade + 5 - (grade % 5)
        dif = next_mul_5 - grade

        if (grade >= 38) and (dif < 3):
            rounded_grades.append(next_mul_5)

        else:
            rounded_grades.append(grade)

    return rounded_grades


if __name__ == "__main__":
    grades_count = int(input())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(*result, sep="\n")
