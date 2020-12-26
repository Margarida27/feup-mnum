# 1. representar a função no Maxima
# 2. verificar o número de raizes
# 3. isolar cada uma das raizes e definir guesses
# 4. definir uma transformada de f(x), t(x),
# 5. atenção ao critério de divergência!! -> se, para qualquer x, dt1/dx(x) < 1 ou dt1/dy(x) < 1, há que definir outra(s) transformada(s)
# 4. escolher critério de paragem
# 5. implementar o método


def check_divergence(x, y, dt1dx, dt1dy, dt2dx, dt2dy):
    if abs(dt1dx(x, y)) + abs(dt2dx(x, y)) < 1 and abs(dt1dy(x, y)) + abs(dt2dy(x, y)) < 1:
        return True
    else:
        return False


def picard_peano_absolute_precision(guess_x, guess_y, e, t1, t2):
    x = guess_x
    y = guess_y
    iterations = 0

    while True:
        xk = t1(x, y)
        yk = t2(x, y)

        if abs(x - xk) < e and abs(y - yk) < e:
            return x, y, iterations

        x = xk
        y = yk
        iterations += 1


def picard_peano_relative_precision(guess_x, guess_y, e, t1, t2):
    x = guess_x
    y = guess_y
    iterations = 0

    while True:
        xk = t1(x, y)
        yk = t2(x, y)

        if abs((x - xk) / x) < e and abs((x - xk) / xk) < e and abs((y - yk) / y) < e and abs((y - yk) / yk) < e:
            return x, y, iterations

        x = xk
        y = yk
        iterations += 1


def picard_peano_func_annulment(guess_x, guess_y, e, f1, t1, f2, t2):
    x = guess_x
    y = guess_y
    iterations = 0

    while True:
        xk = t1(x, y)
        yk = t2(x, y)

        if abs(f1(x, y) - f1(xk, yk)) < e and abs(f2(x, y) - f2(xk, yk)) < e:
            return x, y, iterations

        x = xk
        y = yk
        iterations += 1


def picard_peano_num_iterations(guess_x, guess_y, n, t1, t2):
    x = guess_x
    y = guess_y

    for i in range(n - 1):
        xk = t1(x, y)
        yk = t2(x, y)
        x = xk
        y = yk

    return x, y
