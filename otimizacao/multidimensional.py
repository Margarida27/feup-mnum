import math


# O Método do Gradiente parte de um guess inicial, dando passos proporcionais ao gradiente local,
# desde que resultando em abaixamento da função, até que o mínimo seja atingido.
#
# Esta condição exige a avaliação simultânea:
#     -> do valor do mínimo, verificando se o novo passo não resulta numa variação significativa desse valor;
#     -> isto tanto pode ser consequência de o mínimo ter sido realmente atingido, como de o processo de pesquisa ter atingido uma região de indiferença.
#
#     -> da posição do mínimo, verificando se o novo passo não resulta numa variação significativa dessa posição;
#     -> tanto pode ser consequência de o mínimo ter sido realmente atingido, como de o processo de pesquisa ter atingido um poço.
#
# O método contém em si uma fraqueza:
#     -> o mínimo é, por definição, o ponto em que o gradiente se anula, pelo que os passos na região próxima do mínimo tenderão para zero.


def gradient_method(x, y, h, f, dx, dy, iterations):
    for i in range(iterations):
        xn = x - h * dx(x, y)
        yn = y - h * dy(x, y)
        if f(xn, yn) < f(x, y):
            h *= 2
            x = xn
            y = yn
        else:
            h /= 2
        print("no. iteration: {} -> x = {} y = {} f(x,y) = {} ".format(i, x, y, f(x, y)))


# f(x,y) -> função a minimizar
#
# df_x(x,y) -> função resultante de derivar parcialmente f(x,y) em ordem a x
#
# df_y(x,y) -> função resultante de derivar parcialmente f(x,y) em ordem a y
#
# H(x,y) -> matriz hessiana [df_xx, df_xy]
#                           [df_yx, df_yy]
#
# NO MAXIMA 1) H: invert(hessian(f))
#           2) grad: [diff(f,x),diff(f,y)]
#           3) calcular H.grad
#           4) hx(x,y) = expressão em (H.grad)[1]
#           5) hy(x,y) = expressão em (H.grad)[2]
#
# então -> xn = x - hx(x,y)
#       -> yn = y - hy(x,y)


def quadric_method():
    return


# f(x,y) -> função a minimizar
#
# df_x(x,y) -> função resultante de derivar parcialmente f(x,y) em ordem a x
#
# df_y(x,y) -> função resultante de derivar parcialmente f(x,y) em ordem a y
#
# H(x,y) -> matriz hessiana [df_xx, df_xy]
#                           [df_yx, df_yy]
#
# NO MAXIMA 1) H: invert(hessian(f))
#           2) grad: [diff(f,x),diff(f,y)]
#           3) calcular H.grad
#           4) hx(x,y) = expressão em (H.grad)[1]
#           5) hy(x,y) = expressão em (H.grad)[2]
#
# então -> xn = x - hx(x,y) + lambda * df_x(x,y)
#       -> yn = y - hy(x,y) + lambda * df_y(x,y)
#
# se f(xn,yn) < f(x,y) -> lambda /=2
# senão -> lambda *=2
# para calcular o máximo seria o contrário (if f(xn,yn) > f(x,y) lambda *=2 else lambda /= 2)


def levemberg_method():
    return
