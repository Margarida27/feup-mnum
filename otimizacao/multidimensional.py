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
        if not (f(xn, yn) < f(x,
                              y)):  # se o valor da função não diminuir, h deve ser reduzido e o passo não é efetivado
            h /= 2
        else:  # se o valor da função diminuir, h deve ser aumentado e o passo é efetivado
            x = xn
            y = yn
            h *= 2
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
# detH -> determinante da matriz Hessiana inversa (que varia ao longo do método!)
#
# no Maxima -> H: hessian(matrix) -> H_: invert(H) -> detH: determinant(H_)
#
# então -> xn = x - (df_yy(x, y) * df_x(x, y) - df_xy(x, y) * df_y(x, y)) / detH
#
#       -> yn = y - (-df_yx(x, y) * df_x(x, y) - df_xx(x, y) * df_y(x, y)) / detH


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
# detH -> determinante da matriz Hessiana inversa (que varia ao longo do método!)
#
# no Maxima -> H: hessian(matrix) -> H_: invert(H) -> detH: determinant(H_)
#
# então -> xn = x - (df_yy(x, y) * df_x(x, y) - df_xy(x, y) * df_y(x, y)) / detH - lambda * df_x(x,y)
#
#       -> yn = y - (-df_yx(x, y) * df_x(x, y) - df_xx(x, y) * df_y(x, y)) / detH - lambda * df_y(x,y)
#
# se f(xn,yn) < f(x,y) -> lambda /=2
#
# senão -> lambda *=2


def levemberg_method():
    return
