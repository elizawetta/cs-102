"""Calculator"""
print("Калькулятор работает только с целыми числами и операциями -+;/")
print("Пример ввода:\n1-8*17+13\nВывод: -122")
s = input().replace("+", " + ").replace("-", " - ").replace("/", " / ").replace("*", " * ").split()
d = [s[0]]
for i in s[1:]:
    if i in "+-*/":
        d.append(i)
    elif i.isdigit() and d[-1] in "+-":
        d.append(i)
    elif i.isdigit() and d[-1] in "*" and d[-2] not in "-+*/":
        del d[-1]
        d[-1] = str(int(d[-1]) * int(i))
    elif i.isdigit() and d[-1] in "/" and d[-2] not in "-+*/":
        if int(i) == 0:
            print("ERROR")
            break
        del d[-1]
        d[-1] = str(int(d[-1]) / int(i))
    else:
        print("ERROR")
        break
else:
    d = "".join(d).replace("-", " -").replace("+", " ").split()
    print(sum(map(float, d)))
