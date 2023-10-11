"""Calculator"""


def is_number(num):
    """check string is number"""
    return num.replace("-", "").replace(".", "").isdigit()


print("Калькулятор работает только с целыми числами и операциями -+*/")
print("Пример ввода:\n1-8*17+13\nВывод: -122")

S = input().replace(" ", "").replace("--", "+").replace("++", "+")
if S.count("/+") + S.count("*+") + S.count("*/") + S.count("/*") + S.count("+/") + S.count("+*"):
    S = "-"
S = S.replace("+", " + ").replace("-", " - ").replace("/", " / ").replace("*", " * ")
S = S.replace("/  - ", "/ -").replace("*  - ", "* -").replace("+  - ", "+ -")
if S[0:2] in [" -", " +"]:
    S = "0" + S

S = S.split()
d = [S[0]]
if not all(map(lambda x: (x in "-+*/" or is_number(x)), S)):
    S, d = [], []
elif S[-1] in "*-+/" or S[0] in "-+" or len(S) == 0:
    S, d = [], []
for i in S[1:]:
    if i in "+-*/":
        d.append(i)
    elif is_number(i) and d[-1] in "+-":
        d.append(i)
    elif is_number(i) and d[-1] in "*" and is_number(d[-2]):
        del d[-1]
        d[-1] = str(float(d[-1]) * int(i))
    elif is_number(i) and d[-1] in "/" and is_number(d[-2]):
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
        d = ("".join(d)
            .replace("-+", "-")
            .replace("--", "+")
            .replace("-", " -")
            .replace("+", " ")
            .split()
        )
        print(sum(map(float, d)))
