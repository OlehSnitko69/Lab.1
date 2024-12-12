a = 5
b = 80

if a > b:
    print("Помилка: a повинно бути меншим або дорівнювати b.")
else:
    sum_of_squares = 0

    count = 0

    for i in range(a, b + 1):
        sum_of_squares += i ** 2
        count += 1

    average = sum_of_squares / count

    print(f"Середнє арифметичне квадратів чисел від {a} до {b}: {average}")
