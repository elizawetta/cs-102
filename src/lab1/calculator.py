"""Calculator"""


def is_number(num):
    """check string is number"""
    return num.replace("-", "").replace(".", "").isdigit()


def calc(str_):
    """Calculator function"""
    str_ = str_.replace(" ", "").replace("--", "+").replace("++", "+")
    if (
        str_.count("/+")
        + str_.count("*+")
        + str_.count("*/")
        + str_.count("/*")
        + str_.count("+/")
        + str_.count("+*")
    ):
        return "ERROR"
    str_ = str_.replace("+", " + ").replace("-", " - ").replace("/", " / ").replace("*", " * ")
    str_ = str_.replace("/  - ", "/ -").replace("*  - ", "* -").replace("+  - ", "+ -")
    if str_[0:2] in [" -", " +"]:
        str_ = "0" + str_

    str_ = str_.split()

    if not all(map(lambda x: (x in "-+*/" or is_number(x)), str_)):
        return "ERROR"
    if len(str_) == 0 or str_[-1] in "*-+/" or str_[0] in "-+":
        return "ERROR"

    lst = [str_[0]]
    for i in str_[1:]:
        if i in "+-*/":
            lst.append(i)
        elif is_number(i) and lst[-1] in "+-":
            lst.append(i)
        elif is_number(i) and lst[-1] in "*" and is_number(lst[-2]):
            del lst[-1]
            lst[-1] = str(float(lst[-1]) * float(i))
        elif is_number(i) and lst[-1] in "/" and is_number(lst[-2]):
            if int(i) == 0:
                return "ERROR"
            del lst[-1]
            lst[-1] = str(float(lst[-1]) / float(i))
        else:
            return "ERROR"
    lst = (
        "".join(lst)
        .replace("-+", "-")
        .replace("--", "+")
        .replace("-", " -")
        .replace("+", " ")
        .split()
    )
    return sum(map(float, lst))


if __name__ == "__main__":
    print("Калькулятор работает с операциями -+*/")
    print("Пример ввода:\n1-8*17+13\nВывод: -122")
    print(calc(input()))
