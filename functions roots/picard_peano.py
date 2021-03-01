def picard_peano_absolute_precision(guess, e, t, dt):
    x = guess
    if dt(x) < 0:
        return "divergence criterion failed"
    xk = t(x)
    while abs(x - xk) > e:
        x = xk
        if dt(x) < 0:
            return "divergence criterion failed"
        xk = t(x)
    return x


def picard_peano_relative_precision(guess, e, t, dt):
    x = guess
    if dt(x) < 0:
        return "divergence criterion failed"
    xk = t(x)
    while abs((x - xk) / x) > e or abs((x - xk) / xk) > e:
        x = xk
        if dt(x) < 0:
            return "divergence criterion failed"
        xk = t(x)
    return x


def picard_peano_func_annulment(guess, e, f, t, dt):
    x = guess
    if dt(x) < 0:
        return "divergence criterion failed"
    xk = t(x)
    while abs(f(x) - f(xk)) > e:
        x = xk
        if dt(x) < 0:
            return "divergence criterion failed"
        xk = t(x)
    return x


def picard_peano_num_iterations(guess, n, t, dt):
    x = guess
    if dt(x) < 0:
        return "divergence criterion failed"
    xk = t(x)
    for i in range(n):
        x = xk
        if dt(x) < 0:
            return "divergence criterion failed"
        xk = t(x)
    return x
