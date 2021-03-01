import math as m


# EX 1
def f1(x): return m.sin(x)+x**5-0.2*x+1
def bissection(a,b):
    for i in range(6):
        m = (a+b)/2
        if f1(a)*f1(m) < 0:
            b = m
        else:
            a = m
    return m


# EX 2
def f21(x,y): return x**2-y-1.2
def f21_dx(x,y): return 2*x
def f21_dy(x,y): return -1
def f22(x,y): return -x+y**2-1.0
def f22_dx(x,y): return -1
def f22_dy(x,y): return 2*y
def jacobian(x,y): return (f21_dx(x,y)*f22_dy(x,y))-(f22_dx(x,y)*f21_dy(x,y))
def h(x,y): return ((f21(x,y)*f22_dy(x,y))-(f22(x,y)*f21_dy(x,y)))/jacobian(x,y)
def k(x,y): return ((f22(x,y)*f21_dx(x,y))-(f21(x,y)*f22_dx(x,y)))/jacobian(x,y)
def newton(guess_x, guess_y):
    x = guess_x
    y = guess_y
    for i in range(3):
        print(x,y)
        x_cpy = x
        x = x - h(x,y)
        y = y - k(x_cpy,y)


# EX 3
def f3(x): return m.exp(1.5*x)
def f3_dx(x): return 1.5*m.exp(1.5*x)
def arc(x): return m.sqrt(1+f3_dx(x)**2)
def trapeze(a,b,h):
    n = round((a+b)/h)
    area = arc(a)+arc(b)
    for i in range(1,n):
        area += 2*arc(a+i*h)
    area *= h/2
    return area
def simpson(a,b,h):
    h /= 2
    n = round((a+b)/h)
    area = arc(a)+arc(b)
    for i in range(1,n):
        if i%2:
            area += 4*arc(a+i*h)
        else:
            area += 2*arc(a+i*h)
    area *= h/3
    return area
def qc(a,b,h,op):
    if op == "trapeze":
        s = trapeze(a,b,h)
        s1 = trapeze(a,b,h/2)
        s2 = trapeze(a,b,h/4)
        qc = (s1-s)/(s2-s1)
        return qc
    else:
        s = simpson(a, b, h)
        s1 = simpson(a, b, h / 2)
        s2 = simpson(a, b, h / 4)
        qc = (s1 - s) / (s2 - s1)
        return qc
def err(a,b,h,op):
    if op == "trapeze":
        s1 = trapeze(a,b,h/2)
        s2 = trapeze(a,b,h/4)
        e = (s2-s1)/3
        return e
    else:
        s1 = simpson(a,b,h/2)
        s2 = simpson(a,b,h/4)
        e = (s2-s1)/15
        return e


# EX 4
Ta = 59
def T(t,T): return -0.25*(T-Ta)
def euler(T0, t0, h):
    for i in range(2):
        T0 += h*T(t0,T0)
        t0 += h
    print(T0)


# EX 5
def y(x): return -5*m.cos(x)+m.sin(x)+10
def aurea(x1,x2):
    B = (m.sqrt(5)-1)/2
    A = B**2
    x3 = A*(x2-x1)+x1
    x4 = B*(x2-x1)+x1
    for i in range(3):
        print(x1,x2,x3,x4,y(x1),y(x2),y(x3),y(x4))
        if y(x3) > y(x4):
            x2 = x4
        else:
            x1 = x3


# EX 6
def z(x,y): return 3*x**2-x*y+11*y+y**2-8*x
def z_dx(x,y): return -y+6*x-8
def z_dy(x,y): return 2*y-x+11
def grad(x,y): return z_dx(x,y)+z_dy(x,y)
def gradient(x,y,lambd):
    for i in range(2):
        print(x,y,z(x,y),grad(x,y),lambd)
        xn = x-lambd*z_dx(x,y)
        yn = y-lambd*z_dy(x,y)
        if z(xn,yn) < z(x,y):
            lambd *= 2
            x = xn
            y = yn
        else:
            lambd /= 2



if __name__ == '__main__':
    # EX 1
    # print(bissection(-1,0))
    # est = bissection(-1,0)
    # exact = -0.8417343610266149
    # abs_err = exact - est
    # rel_err = abs_err / exact
    # print(abs_err,rel_err)

    # EX 2
    # newton(1.00000,1.00000)

    # EX 3
    # print(trapeze(0,2,0.25),simpson(0,2,0.25))
    # print(trapeze(0,2,0.25/2),simpson(0,2,0.25/2))
    # print(trapeze(0,2,0.25/4),simpson(0,2,0.25/4))
    # print(qc(0,2,0.25,"trapeze"),qc(0,2,0.25,"simpson"))
    # print(err(0,2,0.25,"trapeze"),err(0,2,0.25,"simpson"))

    # EX 4
    # euler(2,2,0.5)

    # EX 5
    # aurea(2,4)
    # as iterações apresentadas permitem enquadrar o extremo num intervalo em x com amplite x4-x1 = 3.23606797749979 - 2

    # EX 6
    # gradient(2,2,1)



