def rope_absolute_precision(a, b, e, f):
    while abs(a - b) > e:
        w = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(w) < 0:
            b = w
        else:
            a = w
    return w


def rope_relative_precision(a, b, e, f):
    while abs((a - b) / a) > e or abs((a - b) / b) > e:
        w = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(w) < 0:
            b = w
        else:
            a = w
    return w


def rope_func_annulment(a, b, e, f):
    while abs(f(a) - f(b)) > e:
        w = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(w) < 0:
            b = w
        else:
            a = w
    return w


def rope__num_iterations(a, b, n, f):
    for i in range(n):
        w = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(w) < 0:
            b = w
        else:
            a = w
    return w
