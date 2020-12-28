import math as m

# EX 1
def f1(x): return (x-7)**2+x**4
def aurea(x1, x2):
    B = (m.sqrt(5)-1)/2
    A = B**2
    while abs(x2-x1) > 1e-10:
        x3 = x1+A*(x2-x1)
        x4 = x1+B*(x2-x1)
        print(x1,x3,x4,x2)
        if f1(x3) < f1(x4):
            x2 = x4
            x4 = x3
        else:
            x1 = x3
            x3 = x4


# EX 2
def L(x): return m.sqrt(6.25*m.exp(5.0*x)+1)
def trapeze(a,b,h):
    n = round((b+a)/h)
    arc = L(a) + L(b)
    for i in range(1,n):
        arc += 2*L(a+i*h)
    arc *= h/2
    return arc
def simpson(a,b,h):
    h /= 2
    n = round((b+a)/h)
    arc = L(a) + L(b)
    for i in range(1,n):
        if i%2:
            arc += 4*L(a+i*h)
        else:
            arc += 2*L(a+i*h)
    arc *= h/3
    return arc
def qc(a,b,h,op):
    if op == 'trapeze':
        s = trapeze(a,b,h)
        s1 = trapeze(a,b,h/2)
        s2 = trapeze(a,b,h/4)
        qc = (s1-s)/(s2-s1)
        return qc
    else:
        s = simpson(a,b,h)
        s1 = simpson(a,b,h/2)
        s2 = simpson(a,b,h/4)
        qc = (s1-s)/(s2-s1)
        return qc
def error(a,b,h,op):
    if op == 'trapeze':
        s1 = trapeze(a,b,h/2)
        s2 = trapeze(a,b,h/4)
        err = (s2-s1)/3
        return err
    else:
        s1 = simpson(a,b,h/2)
        s2 = simpson(a,b,h/4)
        err = (s2-s1)/15
        return err


# EX 3
def f3(x): return m.exp(x)-x-5
def df3(x): return m.exp(x)-1
def rec_1(x): return m.exp(x)-5
def rec_2(x): return m.log(5+x)
def picard_peano(guess, rec):
    iterations = 0
    xn = rec_1(guess)
    while abs(xn-guess) > 1e-10:
        guess = xn
        iterations += 1
        xn = rec(guess)
    print(guess, iterations)
def newton(guess):
    iterations = 0
    xn = guess - f3(guess)/df3(guess)
    while abs(xn-guess) > 1e-10:
        guess = xn
        iterations += 1
        xn = guess - f3(guess) / df3(guess)
    print(guess, iterations)


# EX 4
a = 30.00000
b = 0.50000
def dCdt(t,T,C): return -m.exp(-b/(T+273))*C
def dTdt(t,T,C): return a*m.exp(-b/(T+273))*C-b*(T-20)
def euler(t,C,T,h):
    while t <= 0.5:
        print(t,C,T)
        Cn = C + dCdt(t,T,C)*h
        Tn = T + dTdt(t,T,C)*h
        t += h
        C = Cn
        T = Tn
def rk4(t,C,T,h):
    for i in range(3):
        print(t,C,T)
        dC_1 = dCdt(t,T,C)*h
        dT_1 = dTdt(t,T,C)*h

        dC_2 = dCdt(t+h/2,T+dT_1/2,C+dC_1/2)*h
        dT_2 = dTdt(t+h/2,T+dT_1/2,C+dC_1/2)*h

        dC_3 = dCdt(t+h/2,T+dT_2/2,C+dC_2/2)*h
        dT_3 = dTdt(t+h/2,T+dT_2/2,C+dC_2/2)*h

        dC_4 = dCdt(t+h,T+dT_3,C+dC_3)*h
        dT_4 = dTdt(t+h,T+dT_3,C+dC_3)*h

        dC = dC_1/6+dC_2/3+dC_3/3+dC_4/6
        dT = dT_1/6+dT_2/3+dT_3/3+dT_4/6

        C += dC
        T += dT
        t += h


# EX 5
def f5(x,y): return -1.1*x*y+12*y+7*x**2-8*x
def df5_dx(x,y): return -1.1*y+14*x-8
def df5_dy(x,y): return 12-1.1*x
def gradient(x0,y0,l):
    for i in range(1):
        x = x0-l*df5_dx(x0,y0)
        y = y0-l*df5_dy(x0,y0)
        if f5(x,y) < f5(x0,y0):
            l *= 2
            x0 = x
            y0 = y
        else:
            l /= 2
        print(f5(x0,y0))


if __name__ == '__main__':
    # EX 1
    # aurea(0.7,2.0)

    # EX 2
    # print(trapeze(0.0,1.0,0.125))
    # print(qc(0.0,1.0,0.125,"trapeze"))
    # print(error(0.0,1.0,0.125,"trapeze"))
    # print(simpson(0.0, 1.0, 0.125))
    # print(qc(0.0, 1.0, 0.125, "simpson"))
    # print(error(0.0, 1.0, 0.125, "simpson"))

    # EX 3
    # picard_peano(-5.0, rec_1)
    # picard_peano(2.0, rec_2)
    # r1 = -4.993216188662221 / valor no Maxima = -4.993216188647903
    # r2 = 1.9368474072553188 / valor no Maxima = 1.936847407220219
    # newton(-5.0)
    # newton(2.0)

    # EX 4
    # euler(0,2.50000,25.00000,0.25000)
    # rk4(0,2.50000,25.00000,0.25000)
    T = 54.254990112319504  # euler(0,2.50000,25.00000,0.25000)
    T1 = 51.77066816246778  # euler(0,2.50000,25.00000,0.25000/2)
    T2 = 50.692054509765555  # euler(0,2.50000,25.00000,0.25000/4)
    qc = (T1-T)/(T2-T1)
    err = T2-T1
    # print(qc,err)  # qc = 2.303254685890371 | err = -1.0786136527022236

    # EX 5
    # gradient(3,1,0.1)
    # r = 4.5101700000000005

