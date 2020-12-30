import math as m


# EX 1
def dTdt(T): return -0.25*(T-37)
def euler(t, T, h):
    for i in range(2):
        T += h*dTdt(T)
        t += h
    print(T)


# EX 2
# NO MAXIMA
# a)
# load(linearalgebra);
# A:matrix([1,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5]);
# B:matrix([-1],[1],[1]);
# M:addcol(A,B);
# M:echelon(M);
# float(%);
# b)
# ...
# M:rowop(M,1,2,1/2);
# M:rowop(M,1,3,-1/6);
# rowop(M,2,3,1);
# c)
# X:matrix([-15],[48],[-30]);
# da:matrix([0.05,0.05,0.05],[0.05,0.05,0.05],[0.05,0.05,0.05]);
# db:matrix([0.05],[0.05],[0.05]);
# dx:invert(A).(db-da.X);


# EX 3
# a)
# dar plot das derivadas das formulas de recorrência no Maxima
# se |derivada|<1 no intervalo da raíz, então a fórmula converge para essa raíz
# b)
def rec(x): return 2*m.log(2*x)
def picard_peano(guess):
    for i in range(2):
        print(guess)
        guess = rec(guess)


# EX 5
# outra vez arroz?


# EX 7
def f(x): return x**3-10*m.sin(x)+2.8
def bissection(a,b):
    for i in range(3):
        m = (a+b)/2
        print(a,m,b)
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m


if __name__ == '__main__':
    # EX 1
    # euler(5,3,0.4)

    # EX 3
    # picard_peano(1.1)
    # resíduo = 1.57691-1.1 = 0.47691

    # EX 7
    # bissection(1.5,4.2)
