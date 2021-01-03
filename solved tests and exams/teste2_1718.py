import math as m


# EX 1
# NO MAXIMA:
# A:matrix([18,-1,1],[3,-5,4],[6,8,29]);
# x:float(invert(A).matrix([1],[2],[3]));
# b:matrix([0.5],[0.5],[0.5]);
# a:matrix([0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,0.5,0.5]);
# r:b-(a.x);
# dx:invert(A).r; <- SOLUÇÃO


# EX 2
def rec_x(x,y,z,t): return -(12*z+2*y+t-76)/24  # solve(6*x+0.5*y+3*z+0.25*t=19,x);
def rec_y(x,y,z,t): return -(5*z+24*x+4*t+44)/60  # solve(1.2*x+3*y+0.25*z+0.2*t=-2.2,y);
def rec_z(x,y,z,t): return -(y-4*x+8*t-36)/16  # solve(-1*x+0.25*y+4*z+2*t=9,z);
def rec_t(x,y,z,t): return -(z+4*y+2*x-15)/8  # solve(2*x+4*y+1*z+8*t=15,t);
def gauss_seidel(x0,y0,z0,t0):
    for i in range(1):
        x = rec_x(x0,y0,z0,t0)
        x0 = x
        y = rec_y(x0,y0,z0,t0)
        y0 = y
        z = rec_z(x0,y0,z0,t0)
        z0 = z
        t = rec_t(x0,y0,z0,t0)
        t0 = t
        print(x0,y0,z0,t0)


# EX 3
def trapeze(values, h):
    result = values[0] + values[len(values)-1]
    for i in range(1,len(values)-1):
        result += 2*values[i]
    result *= h/2
    return result


# EX 4
def simpson():
    e0 = 1.1+4.1+1.2+6.5  # vértices da malha
    e1 = 1.4+2.2+1.5+2.1  # pontos médios dos lados da malha
    e2 = 4.5  # ponto central da malha
    hx = 1.8/2
    hy = 1.8/2
    integral = (hx*hy)/9*(e0+4*e1+16*e2)
    print(integral)


# EX 6
A = 1.5
def dy(v): return v
def dv(t,v): return A+t**2+t*v
def euler(t0,y0,v0,h):
    for i in range(3):
        print(t0,y0)
        y0 += h*dy(v0)
        v0 += h*dv(t0,v0)
        t0 += h
def rk4(t0,y0,v0,h):
    for i in range(3):
        print(t0,y0)
        delta1_y = h*dy(v0)
        delta1_v = h*dv(t0,v0)
        delta2_y = h*dy(v0+delta1_v/2)
        delta2_v = h*dv(t0+h/2,v0+delta1_v/2)
        delta3_y = h*dy(v0+delta2_v/2)
        delta3_v = h*dv(t0+h/2,v0+delta2_v/2)
        delta4_y = h*dy(v0+delta3_v)
        delta4_v = h*dv(t0+h,v0+delta3_v)
        delta_y = delta1_y/6+delta2_y/3+delta3_y/3+delta4_y/6
        delta_v = delta1_v/6+delta2_v/3+delta3_v/3+delta4_v/6
        y0 += delta_y
        v0 += delta_v
        t0 += h


if __name__ == '__main__':
    # EX 2
    # gauss_seidel(1.67969,-1.78160,1.93752,2.10369)

    # EX 3
    # o intervalo mínimo que pode ser atingido quando h/4 = h'' = 0.2
    # uma vez que a tabela não fornece dados para intervalos menores
    # então o intervalo mínimo h = 0.8
    values_1 = [1.16,0.65,0.42]
    h1 = 0.8
    s1 = trapeze(values_1,h1)
    values_2 = [1.16,1.08,0.65,1.24,0.42]
    h2 = 0.8/2
    s2 = trapeze(values_2,h2)
    values_3 = [1.16,0.45,1.08,0.53,0.65,1.32,1.24,1.18,0.42]
    h3 = h1/4
    s3 = trapeze(values_3,h3)
    err = (s3-s2)/3
    # print(s1,err)

    # EX 4
    # simpson()

    # EX 6
    # euler(1,0,1,0.2)
    # rk4(1,0,1,0.2)
