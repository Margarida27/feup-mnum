# método de 2a ordem
def trapeze_method(xi, xf, n, f):
    h = (xf - xi) / n
    area = f(xi) + f(xf)
    for i in range(1, n):
        area += 2 * f(xi + i * h)
    area *= h / 2
    return area


# e = (S'' - S') / (2 * order_number - 1) -> neste caso order_number = 2
# S'' - S' = 3 * e''
# S'' <=> solução com h'' = h / 4 (n * 4)
# S' <=> solução com h' = h / 2 (n * 2)
def trapeze_abs_error(xi, xf, n, f):
    s1 = trapeze_method(xi, xf, n * 2, f)
    s2 = trapeze_method(xi, xf, n * 4, f)
    e = (s2 - s1) / 3
    return e


def trapeze_rel_error(xi, xf, n, f):
    s2 = trapeze_method(xi, xf, n * 4, f)
    abs_error = trapeze_abs_error(xi, xf, n, f)
    rel_error = abs_error / s2
    return rel_error


# QC = (S' - S) / (S'' - S')
# QC = 2 * order_number -> neste caso order_number = 2 -> QC = 4
# S'' <=> solução com h'' = h / 4 (n * 4)
# S' <=> solução com h' = h / 2 (n * 2)
def trapeze_qc(xi, xf, n, f):
    s = trapeze_method(xi, xf, n, f)
    s1 = trapeze_method(xi, xf, n * 2, f)
    s2 = trapeze_method(xi, xf, n * 4, f)
    qc = (s1 - s) / (s2 - s1)
    return qc
