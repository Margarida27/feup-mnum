# 1. representar a função no Maxima
# 2. verificar o número de raizes
# 3. isolar cada uma das raizes e definir guesses
# 4. escolher critério de paragem
# 5. implementar o método
# 6. atenção ao critério de divergência!! -> derivada da função não pode ser nula


def newton_absolute_precision(guess, e, f, df):
    x = guess
    if df(x) == 0:
        return "divergence criterion failed"
    xk = x - f(x) / df(x)

    while abs(x - xk) > e:
        x = xk
        if df(x) == 0:
            return "divergence criterion failed"
        xk = x - f(x) / df(x)
    return x

def newton_relative_precision(guess, e, f, df):
    x = guess
    if df(x) == 0:
        return "divergence criterion failed"
    xk = x - f(x) / df(x)

    while abs((x - xk) / x) > e or abs((x - xk) / xk) > e:
        x = xk
        if df(x) == 0:
            return "divergence criterion failed"
        xk = x - f(x) / df(x)
    return x

def newton_func_annulment(guess, e, f, df):
    x = guess
    if df(x) == 0:
        return "divergence criterion failed"
    xk = x - f(x) / df(x)

    while abs(f(x) - f(xk)) > e:
        x = xk
        if df(x) == 0:
            return "divergence criterion failed"
        xk = x - f(x) / df(x)
    return x

def newton_num_iterations(guess, n, f, df):
    x = guess
    if df(x) == 0:
        return "divergence criterion failed"
    xk = x - f(x) / df(x)

    for i in range(n):
        x = xk
        if df(x) == 0:
            return "divergence criterion failed"
        xk = x - f(x) / df(x)
    return x
