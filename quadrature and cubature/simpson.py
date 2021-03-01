# método de 4a ordem
def simpson_method(xi, xf, n, f):
    h = (xf - xi) / (2 * n)
    area = f(xi) + f(xf)
    for i in range(1, 2 * n):
        if i % 2:
            area += 2 * f(xi + i * h)
        else:
            area += 4 * f(xi + i * h)
    area *= h / 3
    return area


# e = (S'' - S') / (2 * order_number - 1) -> neste caso order_number = 4
# S'' - S' = 15 * e''
# S'' <=> solução com h'' = h / 4 (n * 4)
# S' <=> solução com h' = h / 2 (n * 2)
def simpson_abs_error(xi, xf, n, f):
    s1 = simpson_method(xi, xf, n * 2, f)
    s2 = simpson_method(xi, xf, n * 4, f)
    e = (s2 - s1) / 3
    return e


def simpson_rel_error(xi, xf, n, f):
    s2 = simpson_method(xi, xf, n * 4, f)
    abs_error = simpson_method(xi, xf, n, f)
    rel_error = abs_error / s2
    return rel_error


# QC = (S' - S) / (S'' - S')
# QC = 2 * order_number -> neste caso order_number = 4 -> QC = 16
# S'' <=> solução com h'' = h / 4 (n * 4)
# S' <=> solução com h' = h / 2 (n * 2)
def simpson_qc(xi, xf, n, f):
    s = simpson_method(xi, xf, n, f)
    s1 = simpson_method(xi, xf, n * 2, f)
    s2 = simpson_method(xi, xf, n * 4, f)
    qc = (s1 - s) / (s2 - s1)
    return qc
