import math


# EX 1
def f1(x):
    return math.sin(x)+x**5-0.2*x+1
def bissection(a,b):
    while abs(b-a) > 1e-10:
        m = (b+a) / 2.0
        if f1(a)*f1(b) < 0:
            b = m
        else:
            a = m
    return m


# EX 2
def g1(x,y):
    return x**2-y-1.2
def g1dx(x,y):
    return 2*x
def g1dy(x,y):
    return -1
def g2(x,y):
    return -x+y**2-1.0
def g2dx(x,y):
    return -1
def g2dy(x,y):
    return 2*y
def J(x,y):
    return g1dx(x,y) * g2dy(x,y) - g2dx(x,y) * g1dy(x,y)
def hn(x,y):
    return (g1(x,y) * g2dy(x,y) - g2(x,y) * g1dy(x,y)) / J(x,y)
def hk(x,y):
    return (g2(x,y) * g1dx(x,y) - g1(x,y) * g2dx(x,y)) / J(x,y)
def newton(x0,y0):
    x = x0
    y = y0
    for i in range(30):
        x_cpy = x
        x -= hn(x,y)
        y -= hk(x_cpy,y)
    return x,y


# EX 3
def f3(x):
    return math.sqrt(1+(1.5*math.exp(1.5*x))**2)
def trapeze(a,b,h):
    n = round((b-a)/h)
    l = f3(a) + f3(b)
    for i in range(1,n):
        l += 2*f3(a+i*h)
    l *= h/2
    return l
def simpson(a,b,h):
    h /= 2
    n = round((b-a)/h)
    l = f3(a) + f3(b)
    for i in range(1,n):
        if i % 2:
            l += 4*f3(a+i*h)
        else:
            l += 2*f3(a+i*h)
    l *= h/3
    return l
def ex3_error(a,b,h,method):
    if method == 1:
        s1 = simpson(a,b,h/2.0)
        s2 = simpson(a,b,h/4.0)
        error = (s2-s1)/15.0
    if method == 2:
        s1 = trapeze(a,b,h/2.0)
        s2 = trapeze(a,b,h/4.0)
        error = (s2-s1)/3.0
    return error
def ex3_qc(a,b,h,method):
    if method == 1:
        s = simpson(a,b,h)
        s1 = simpson(a,b,h/2.0)
        s2 = simpson(a,b,h/4.0)
    if method == 2:
        s = trapeze(a,b,h)
        s1 = trapeze(a,b,h/2.0)
        s2 = trapeze(a,b,h/4.0)
    qc = (s1-s)/(s2-s1)
    return qc


# EX 4
def f4(t,T):
    return -0.25*(T-59)
def euler(t0,T0,h):
    for i in range(2):
        T0 += f4(t0,T0)*h
        t0 += h
    return T0


# EX 5
def f5(x):
    return -5*math.cos(x)+math.sin(x)+10
def aurea(x1,x2,x3,x4):
    print("x1 = {}     x2 = {}     x3 = {}     x4 = {}     f(x1) = {}     f(x2) = {}     f(x3) = {}     f(x4) = {}\n".format(x1,x2,x3,x4,f5(x1),f5(x2),f5(x3),f5(x4)))
    B = (math.sqrt(5) - 1) / 2
    A = B**2
    for i in range(3):
        if f5(x3) > f5(x4):
            x2 = x4
            x4 = B*(x2-x1)+x1
        else:
            x1 = x3
            x3 = A*(x2-x1)+x1
        print("x1 = {}     x2 = {}     x3 = {}     x4 = {}     f(x1) = {}     f(x2) = {}     f(x3) = {}     f(x4) = {}\n".format(x1,x2,x3,x4,f5(x1),f5(x2),f5(x3),f5(x4)))

# EX 6
def f6(x,y):
    return 3*x**2-x*y+11*y**2-8*x
def f6dx(x,y):
    return -y+6*x-8
def f6dy(x,y):
    return 22*y-x
def gradient(x, y, lambd):
    for i in range(30):
        print("x = {}     y = {}     f(x,y) = {}\ngradient = {}     lambda = {}".format(x, y, f6(x,y), f6dx(x,y)+f6dy(x,y), lambd))

        xn = x-lambd*f6dx(x,y)
        yn = y-lambd*f6dy(x,y)

        print("precision = {}\n".format(abs(xn-x)))

        if f6(xn,yn) < f6(x,y):
            lambd *= 2
            x = xn
            y = yn
        else:
            lambd /= 2


if __name__ == '__main__':
    print(bissection(-1,0))

    print(newton(1.00000,1.00000))
    print(newton(0.20000,-1.1000))

    print(trapeze(0, 2, 0.25))
    print(ex3_qc(0, 2, 0.25, 2))  # qc trapeze
    print(ex3_error(0, 2, 0.25, 2))  # error trapeze

    print(simpson(0,2,0.25))
    print(ex3_qc(0,2,0.25,1))  # qc simpson
    print(ex3_error(0,2,0.25,1))  # error simpson

    print(euler(2,2,0.5))

    print(aurea(2,4,2.76393,3.23606))

    print(gradient(2, 2, 0.50))