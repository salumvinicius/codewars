def zero(arg = None):
    if arg is None:
        return 0
    else:
        return arg(0)
def one(arg = None):
    if arg is None:
        return 1
    else:
        return arg(1)
def two(arg = None):
    if arg is None:
        return 2
    else:
        return arg(2)
def three(arg = None):
    if arg is None:
        return 3
    else:
        return arg(3)
def four(arg = None):
    if arg is None:
        return 4
    else:
        return arg(4)
def five(arg = None):
    if arg is None:
        return 5
    else:
        return arg(5)
def six(arg = None):
    if arg is None:
        return 6
    else:
        return arg(6)
def seven(arg = None):
    if arg is None:
        return 7
    else:
        return arg(7)
def eight(arg = None):
    if arg is None:
        return 8
    else:
        return arg(8)
def nine(arg = None):
    if arg is None:
        return 9
    else:
        return arg(9)
​
def plus(numero):
    return lambda x: x + numero
def minus(numero):
    return lambda x: x - numero
def times(numero):
    return lambda x: x * numero
def divided_by(numero):
    return lambda x: x // numero