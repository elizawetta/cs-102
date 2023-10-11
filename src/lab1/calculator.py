"""Calculator"""
print("Калькулятор работает только с целыми числами и операциями -+*/")
print("Пример ввода:\n1-8*17+13\nВывод: -122")

s = input().replace("+", " + ").replace("-", " - ").replace("/", " / ").replace("*", " * ").split()
d = [s[0]]
if not all(map(lambda x: (x in "-+*/" or x.isdigit()), s)) or s[-1] in "*-+/" or len(s) == 0:
    s, d = [], []
for i in s[1:]:
    if i in "+-*/":
        d.append(i)
    elif i.isdigit() and d[-1] in "+-":
        d.append(i)
    elif i.isdigit() and d[-1] in "*" and d[-2].replace(".", "").isdigit():
        del d[-1]
        d[-1] = str(float(d[-1]) * int(i))
    elif i.isdigit() and d[-1] in "/" and d[-2].replace(".", "").isdigit():
        if int(i) == 0:
            print("ERROR")
            break
        del d[-1]
        d[-1] = str(float(d[-1]) / int(i))
    else:
        print("ERROR")
        break
else:
    if len(d) == 0:
        print("ERROR")
    else:
        d = "".join(d).replace("-", " -").replace("+", " ").split()
        print(sum(map(float, d)))
