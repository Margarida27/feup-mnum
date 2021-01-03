import math as m

# EX 1
def f(x): return m.exp(x)-x-2-4
def df(x): return m.exp(x)-1
def rec_newton(x): return x-f(x)/df(x)
def newton(x):
    it = 0
    while True:
        xk = rec_newton(x)
        it += 1
        if abs(x - xk) < 1e-5:
            return it, x
        x = xk

def rec1(x): return m.exp(x)-2-4
def rec2(x): return m.log(4+x+2)
def pp1(x):  # using rec1
    it = 0
    while True:
        xk = rec1(x)
        if abs(xk - x) < 1e-5:
            return it, x
        it += 1
        x = xk
def pp2(x):  # using rec2
    it = 0
    while True:
        xk = rec2(x)
        if abs(xk - x) < 1e-5:
            return it, x
        it += 1
        x = xk

if __name__ == '__main__':
    # EX 1
    # NO MAXIMA
    # f:%e^x-x-2-4;
    # dado que f(-inf) = +inf e f(+inf) = +inf, nada podemos concluir
    # df:diff(f,x);
    # solve(df,x); # [x = 0]
    # subst(x=0,f); # -5
    # daqui resulta que a equação tem pelo menos duas raízes, uma no intervalo [-inf, 0] e outra no intervalo [0, +inf]
    # os intervalos podem ser definidos, pela a análise do gráfico, por:
    # raiz 1 -> [-6.3,-5.6]
    # raiz 2 -> [1.7, 2.7]

    # print(newton(-5.9))
    # print(pp1(-5.9))
    # print(pp2(-5.9))
    # print(newton(3.0))
    # print(pp1(3.0))


