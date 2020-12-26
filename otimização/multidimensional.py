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


# seja f(x,y) a função a minimizar
# seja dfx(x,y) a função resultante de derivar parcialmente f(x,y) em ordem a x
# seja dfy(x,y) a função resultante de derivar parcialmente f(x,y) em ordem a y
# seja H(x,y) a sua matriz hessiana [[dfxx, dfxy],
#                                    [dfyx, dfyy]]
# seja detH o determinante da matriz Hessiana inversa (que varia ao longo do método!)
# então xn = x - (dfyy(x, y) * dfx(x, y) - dfxy(x, y) * dfy(x, y)) / detH
#       yn = y - (-dfxy(x, y) * dfx(x, y) - dfxx(x, y) * dfy(x, y)) / detH


def quadric_method():
    return


# escolhendo um lambda
# seja f(x,y) a função a minimizar
# seja dfx(x,y) a função resultante de derivar parcialmente f(x,y) em ordem a x
# seja dfy(x,y) a função resultante de derivar parcialmente f(x,y) em ordem a y
# seja H(x,y) a sua matriz hessiana [[dfxx, dfxy],
#                                    [dfyx, dfyy]]
# seja detH o determinante da matriz Hessiana inversa (que varia ao longo do método!)
# então xn = x - (dfyy(x, y) * dfx(x, y) - dfxy(x, y) * dfy(x, y)) / detH - lambda * dfx(x,y)
#       yn = y - (-dfxy(x, y) * dfx(x, y) - dfxx(x, y) * dfy(x, y)) / detH - lambda * dfx(x,y)
# se f(x,y) > f(xn,yn) -> lambda /=2 e o passo não é efetivado
# senão lambda *=2 e x = xn e y = yn


def levemberg_method():
    return
