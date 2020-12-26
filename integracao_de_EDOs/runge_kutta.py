PRECISION = 10e-10


# método de 2a ordem
# dy = f(x,y,z)
def rk2_method(x0, y0, x, h, df):
    while abs(x - x0) > PRECISION:
        ya = df(x0 + h / 2, y0 + df(x0, y0) * h / 2)
        y0 += ya * h
        x0 += h
    return y0


# dy = f(x,y,z)
# dz = f(x,y,z)
def rk2_system_method(x0, y0, z0, x, h, dy, dz):
    while abs(x - x0) > PRECISION:
        ya = dy(x0 + h / 2, y0 + dy(x0, y0) * h / 2)
        za = dz(x0 + h / 2, y0 + dz(x0, y0) * h / 2)
        y0 += ya * h
        z0 += za * h
        x0 += h
    return y0


# método de 4a ordem
# dy = f(x, y)
def rk4_method(x0, y0, x, h, dy):
    while abs(x - x0) > PRECISION:
        delta1 = h * dy(x0, y0)
        delta2 = h * dy(x0 + h / 2, y0 + delta1 / 2)
        delta3 = h * dy(x0 + h / 2, y0 + delta2 / 2)
        delta4 = h * dy(x0 + h, y0 + delta3)

        delta_y = delta1 / 6 + delta2 / 3 + delta3 / 3 + delta4 / 6

        x0 += h
        y0 += delta_y
    return y0


# dy = f(x,y,z)
# dz = f(x,y,z)
def rk4_system_method(x0, y0, z0, x, h, dy, dz):
    while abs(x - x0) > PRECISION:
        delta1_y = h * dy(x0, y0)
        delta1_z = h * dz(x0, y0)

        delta2_y = h * dy(x0 + h / 2, y0 + delta1_y / 2)
        delta2_z = h * dz(x0 + h / 2, y0 + delta1_z / 2)

        delta3_y = h * dy(x0 + h / 2, y0 + delta2_y / 2)
        delta3_z = h * dz(x0 + h / 2, y0 + delta2_z / 2)

        delta4_y = h * dy(x0 + h, y0 + delta3_y)
        delta4_z = h * dz(x0 + h, y0 + delta3_z)

        delta_y = delta1_y / 6 + delta2_y / 3 + delta3_y / 3 + delta4_y / 6
        delta_z = delta1_z / 6 + delta2_z / 3 + delta3_z / 3 + delta4_z / 6

        x0 += h
        y0 += delta_y
        z0 += delta_z
    return y0


# QC = (S' - S) / (S'' - S')
# QC = 2 * order_number -> neste caso order_number = 2 -> QC = 4
# S'' <=> solução com h'' = h / 4
# S' <=> solução com h' = h / 2
def rk2_qc(x0, y0, x, h, df):
    s = rk2_method(x0, y0, x, h, df)
    s1 = rk2_method(x0, y0, x, h / 2, df)
    s2 = rk2_method(x0, y0, x, h / 4, df)
    qc = (s1 - s) / (s2 - s1)
    return qc


# e = (S'' - S') / (2 * order_number - 1) -> neste caso order_number = 2
# S'' - S' = 3 * e''
# S'' <=> solução com h'' = h / 4
# S' <=> solução com h' = h / 2
def rk2_error(x0, y0, x, h, df):
    s1 = rk2_method(x0, y0, x, h / 2, df)
    s2 = rk2_method(x0, y0, x, h / 4, df)
    error = (s2 - s1) / 3
    return error


# QC = (S' - S) / (S'' - S')
# QC = 2 * order_number -> neste caso order_number = 4 -> QC = 16
# S'' <=> solução com h'' = h / 4
# S' <=> solução com h' = h / 2
def rk4_qc(x0, y0, x, h, df):
    s = rk4_method(x0, y0, x, h, df)
    s1 = rk4_method(x0, y0, x, h / 2, df)
    s2 = rk4_method(x0, y0, x, h / 4, df)
    qc = (s1 - s) / (s2 - s1)
    return qc


# e = (S'' - S') / (2 * order_number - 1) -> neste caso order_number = 4
# S'' - S' = 15 * e''
# S'' <=> solução com h'' = h / 4
# S' <=> solução com h' = h / 2
def rk4_error(x0, y0, x, h, df):
    s1 = rk4_method(x0, y0, x, h / 2, df)
    s2 = rk4_method(x0, y0, x, h / 4, df)
    error = (s2 - s1) / 15
    return error

# como resolver equações de ordem superior?
# suponhamos que temos a seguinte equação:
#
#             y'' = f(x,y,y') (equação de 2a ordem)
#
# pode reduzir-se a um sistema de duas equações de 1a ordem, o qual já sabemos resolver
#
#             z' = f(x,y,z)
#             y' = z
#
# um exemplo mais avançado:
#
#             y'' = f(x,y,y',z,z')
#             z'' = g(x,y,y',z,z')
#
#                      <=>
#
#             u' = f(x,y,u,z,v)
#             y' = u
#             v' = g(x,y,u,z,v)
#             z' = v
