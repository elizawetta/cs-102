a = "0"
print("Введите Enter что бы закончить")
while a:
    a = input("Введите первое число: ")
    if a == "":
        break
    while not a.replace(".", "").isdigit() or a.count(".") > 1:
        print("Это не число!!")
        a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    while not b.replace(".", "").isdigit() or b.count(".") > 1:
        print("Это не число!!")
        b = input("Введите второе число: ")
    s = input("Введите операцию(+-*/): ")
    while s not in ["+", "-", "*", "/"]:
        print("Операция некорректна!!")
        b = input("Введите корректную операцию(+-*/): ")
    a1, b1 = float(a), float(b)

    if b1 == 0 and s == "/":
        print("Деление на 0 невозможно")
    elif s == "-":
        print(a1 - b1)
    elif s == "+":
        print(a1 + b1)
    elif s == "*":
        print(a1 * b1)
    elif s == "/":
        print(a1 / b1)
