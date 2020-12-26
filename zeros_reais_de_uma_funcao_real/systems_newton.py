# 1. representar a função no Maxima
# 2. verificar o número de raizes
# 3. isolar cada uma das raizes e definir guesses
# 4. escolher critério de paragem
# 5. implementar o método


def newton_absolute_precision(guess_x, guess_y, e, f1, df1dx, df1dy, f2, df2dx, df2dy):
    x = guess_x
    y = guess_y
    iterations = 0

    while True:
        jacobian = df1dx(x, y) * df2dy(x, y) - df2dx(x, y) * df1dy(x, y)
        xn = x - (f1(x, y) * df2dy(x, y) - f2(x, y) * df1dy(x, y)) / jacobian
        yn = y - (f2(x, y) * df1dx(x, y) - f1(x, y) * df2dx(x, y)) / jacobian

        if abs(x - xn) < e and abs(y - yn) < e:
            return x, y, iterations

        x = xn
        y = yn
        iterations += 1


def newton_relative_precision(guess_x, guess_y, e, f1, df1dx, df1dy, f2, df2dx, df2dy):
    x = guess_x
    y = guess_y
    iterations = 0

    while True:
        jacobian = df1dx(x, y) * df2dy(x, y) - df2dx(x, y) * df1dy(x, y)
        xn = x - (f1(x, y) * df2dy(x, y) - f2(x, y) * df1dy(x, y)) / jacobian
        yn = y - (f2(x, y) * df1dx(x, y) - f1(x, y) * df2dx(x, y)) / jacobian

        if abs((x - xn) / x) < e and abs((x - xn) / xn) < e and abs((y - yn) / y) < e and abs((y - yn) / yn) < e:
            return x, y, iterations

        x = xn
        y = yn
        iterations += 1


def newton_func_annulment(guess_x, guess_y, e, f1, df1dx, df1dy, f2, df2dx, df2dy):
    x = guess_x
    y = guess_y
    iterations = 0

    while True:
        jacobian = df1dx(x, y) * df2dy(x, y) - df2dx(x, y) * df1dy(x, y)
        xn = x - (f1(x, y) * df2dy(x, y) - f2(x, y) * df1dy(x, y)) / jacobian
        yn = y - (f2(x, y) * df1dx(x, y) - f1(x, y) * df2dx(x, y)) / jacobian

        if abs(f1(x, y) - f1(xn, yn)) < e and abs(f2(x, y) - f2(xn, yn)) < e:
            return x, y, iterations

        x = xn
        y = yn
        iterations += 1


def newton_num_iterations(guess_x, guess_y, n, f1, df1dx, df1dy, f2, df2dx, df2dy):
    x = guess_x
    y = guess_y

    for i in range(n - 1):
        jacobian = df1dx(x, y) * df2dy(x, y) - df2dx(x, y) * df1dy(x, y)
        xn = x - (f1(x, y) * df2dy(x, y) - f2(x, y) * df1dy(x, y)) / jacobian
        yn = y - (f2(x, y) * df1dx(x, y) - f1(x, y) * df2dx(x, y)) / jacobian
        x = xn
        y = yn

    return x, y
