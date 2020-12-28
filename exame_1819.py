import math as m

# EX 1


def f11(x,y): return m.sin(x+y)-m.exp(x-y)
def df11_dx(x,y): return m.cos(x+y)-m.exp(x-y)
def df11_dy(x,y): return m.cos(x+y)+m.exp(x-y)
def f12(x,y): return m.cos(x+y)-x**2*y**2
def df12_dx(x,y): return -m.sin(x+y)-2*x*y**2
def df12_dy(x,y): return -m.sin(x+y)-2*x**2*y
def jacobian(x,y): return df11_dx(x,y)*df12_dy(x,y)-df12_dx(x,y)*df11_dy(x,y)
def hn(x,y): return f11(x,y)*df12_dy(x,y)-f12(x,y)*df11_dy(x,y) / jacobian(x,y)
def kn(x,y): return f12(x,y)*df11_dx(x,y)-f11(x,y)*df12_dx(x,y) / jacobian(x,y)
def newton(x0,y0):
    x = x0
    y = y0
    for i in range(3):
        print(x, y)
        xn = x-hn(x,y)
        yn = y-kn(x,y)
        x = xn
        y = yn


# EX 2
def rec_x(x,y,z): return -(205*z+305*y-6)/515
def rec_y(x,y,z): return -(6*z+2*x)/11
def rec_z(x,y,z): return -(10*y+2*x+13)/13
def gauss_seidel(x,y,z):
    for i in range(30):
        print(x,y,z)
        xn = rec_x(x,y,z)
        x = xn
        yn = rec_y(xn,y,z)
        y = yn
        zn = rec_z(xn,yn,z)
        z = zn


# EX 3
def simpson():
    hx = (2-0)/2
    hy = (2-0)/2
    e0 = 1.1+9.8+7.8+1.2  # vértices da malha
    e1 = 1.4+1.5+2.1+2.2  # pontos médios dos lados da malha
    e2 = 4  # valor no centro da malha
    area = (hx*hy)/9*(e0+4*e1+16*e2)
    print(area)


# EX 4
# y'' = f(x,y,y'') = A * y' - B * y  <=>  z' = f(x,y,z) = A * z - B * y
#                                         y' = z
A = -7
B = 4
def dz(x,y,z): return A*z-B*y
def dy(x,y,z): return z
def euler(x,y,z,h):
    for i in range(4):
        print(x,y,z)
        z_cpy = z
        z += h*dz(x,y,z)
        y += h*dy(x,y,z_cpy)
        x += h


# EX 5
def f5(x): return (x-7)**2+x**4
def aurea(x1,x2):
    B = (m.sqrt(5)-1)/2
    A = B**2
    for i in range(20):
        x3 = x1+A*(x2-x1)
        x4 = x1+B*(x2-x1)
        print(x1,x3,x4,x2)
        if f5(x3) < f5(x4):
            x2 = x4
            x4 = x3
        else:
            x1 = x3
            x3 = x4


if __name__ == '__main__':
    # EX 1
    # newton(0.500000,0.250000)

    # EX 2
    # gauss_seidel(0.150000,0.900000,1.700000)

    # EX 3
    # simpson()
    # 12.522222222222222

    # EX 4
    # euler(0.40000,2.00000,1.00000,0.2)
    # sabendo que h = delta_x, basta olhar para a tabela e conseguimos obter h e o valor de x da 1a linha

    # EX 5
    # aurea(0.7,2.0)
    # dado que f é uma função unidimensional poderíamos optar por: trisseção, regra dos terços, regra áurea

    # EX 6
    a = 0.4523e4
    b = 0.2115e-3
    c = 0.2583e1
    exact = a+b+c  # = 4525.583211499999
    aprox = 0.4525e4
    abs_error = abs(exact-aprox)
    rel_error = abs_error/exact
    print(aprox, abs_error, rel_error)
