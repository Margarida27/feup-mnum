PRECISION = 10e-10


def euler_method(x0, y0, x, h, df):
    while abs(x - x0) > PRECISION:
        y0 += df(x0, y0) * h
        x0 += h
    return y0


def modified_euler_method():
    return


# QC = (S' - S) / (S'' - S')
# QC = 2 * order_number -> neste caso order_number = 1 -> QC = 2
# S'' <=> solução com h'' = h / 4
# S' <=> solução com h' = h / 2
def euler_qc(x0, y0, x, h, df):
    s = euler_method(x0, y0, x, h, df)
    s1 = euler_method(x0, y0, x, h / 2, df)
    s2 = euler_method(x0, y0, x, h / 4, df)
    qc = (s1 - s) / (s2 - s1)
    return qc


# e = (S'' - S') / (2 * order_number - 1) -> neste caso order_number = 1
# S'' - S' = e''
# S'' <=> solução com h'' = h / 4
# S' <=> solução com h' = h / 2
def euler_error(x0, y0, x, h, df):
    s1 = euler_method(x0, y0, x, h / 2, df)
    s2 = euler_method(x0, y0, x, h / 4, df)
    error = s2 - s1
    return error
