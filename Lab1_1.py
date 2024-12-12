a = float(input("Введіть число a (додатнє): "))
b = float(input("Введіть число b (додатнє): "))

if a <= 0 or b <= 0:
    print("Числа a та b повинні бути додатніми!")
else:
    if a > b:
        x = b / a + 61
    elif a == b:
        x = -5
    else:
        x = (b - a) / b

    print(f"Значення X: {x}")
