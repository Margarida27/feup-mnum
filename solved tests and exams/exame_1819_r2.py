import math as m


# EX 1
def f1(x,y): return m.sin(x+y)-m.exp(x-y)
def f1_dx(x,y): return m.cos(x+y)-m.exp(x-y)
def f1_dy(x,y): return m.cos(x+y)+m.exp(x-y)
def f2(x,y): return m.cos(x+y)-x**2*y**2
def f2_dx(x,y): return -m.sin(x+y)-2*x*y**2
def f2_dy(x,y): return -m.sin(x+y)-2*x**2*y
def jacobian(x,y): return (f1_dx(x,y)*f2_dy(x,y))-(f2_dx(x,y)*f1_dy(x,y))
def h(x,y): return ((f1(x,y)*f2_dy(x,y))-(f2(x,y)*f1_dy(x,y)))/jacobian(x,y)
def k(x,y): return ((f2(x,y)*f1_dx(x,y))-(f1(x,y)*f2_dx(x,y)))/jacobian(x,y)
def newton(x,y):
    for i in range(3):
        print(x,y)
        x_cpy = x
        x = x-h(x,y)
        y = y-k(x_cpy,y)


# EX 3
def simpson():
    e1 = 1.1+9.8+7.8+1.2
    e2 = 1.4+2.2+1.5+2.1
    e3 = 4
    hx = 1
    hy = 1
    integral = (hx*hy)/9*(e1+4*e2+16*e3)
    print(integral)


# EX 4
A = -7
B = 4
def dy(x,y,z): return z
def dz(x,y,z): return A*dy(x,y,z)-B*y
def euler(x,y,z,h):
    for i in range(4):
        print(x,y,z)
        z_cpy = z
        z += h*dz(x,y,z)
        y += h*dy(x,y,z_cpy)
        x += h


# EX 5
a = 0
def y(x): return (x-a)**2+x**4
def aurea(x1,x2):
    B = (m.sqrt(5)-1)/2
    A = B**2
    while True:
        x3 = A * (x2-x1)+x1
        x4 = B * (x2-x1)+x1
        if abs(x4-x1) < 1e-5 and abs(x2-x3) < 1e-5:
            break
        if y(x3) < y(x4):
            x2 = x4
        else:
            x1 = x3

    min = x1
    if y(x3) < y(x1): min = x2
    if y(x4) < y(x1): min = x4
    if y(x2) < y(x1): min = x1
    print(min)

if __name__ == '__main__':
    # EX 1
    print("EX 1 - NEWTON")
    newton(0.500000,0.250000)

    # EX 2
    print("\n\nEX 2 - SISTEMA DE EQUAÇÕES")
    print("a) Sistema 1 porque é o único com diagonal dominante.\n")
    print("b) ?\n")
    print("c) xn = xn = (205*z+305*y-6)/515\n"
          "   yn = (-6*z+2*xn)/11\n"
          "   zn = (-10*yn-2*xn)/13\n")

    # EX 3
    print("\n\nEX 3 - SIMPSON")
    simpson()

    # EX 4
    print("\n\nEX 4 - EULER")
    euler(0.40000,2.00000,1.00000,0.200000)

    # EX 5
    print("\n\nEX 5 - MINIMO")
    aurea(-0.1,0.1)

    # Dado que se trata de uma função unidimensional, dispomos dos seguintes métodos para a sua resolução:

    # ------------ PESQUISA UNIDIMENSIONAL ------------
    # Consiste em procurar, a partir de um ponto de partida dado, o sentido em que a função decresce. Em seguida
    # efetua-se um passo nesse sentido, e assim sucessivamente, até se detetar um aumento na função, isto é, que
    # o novo valor calculado seja mais alto que o anterior. Quando tal se verificar, abandonam-se os dois últimos
    # pontos calculados e parte-se de novo do antepenúltimo, mas agora com um passo menor, por exemplo, metade do
    # anterior. O processo prossegue até o mínimo ter sido localizado dentro da precisão pré-especificada. A grande
    # vantagem deste método é a de permitir que a partir de um guess se obtenha um intervalo enquadrante do mínimo,
    # que facilita a aplicação dos métodos a seguir.

    # ------------ MÉTODO DOS TERÇOS ------------
    # Este método intervalar de minimização caracteriza-se por fazer a divisão do intervalo enquadrante em três
    # subintervalos iguais. Suponhamos que são conhecidos dois pontos, x1 e x2, entre os quais se encontra o mínimo
    # procurado. A partir daí calculam-se dois novos pontos x3 e x4 dentro do intervalo [x1, x2]; se f(x4) < f(x3),
    # podemos garantir que o mínimo se encontra entre x3 e x2, de modo que não há necessidade de pesquisar no intervalo
    # [x1, x3]; do mesmo modo, se f(x3) < f(x4), podemos abandonar [x4, x2]. Uma desvantagem deste método deve-se ao
    # facto de, quando se abandona um dos subintervalos, nenhum dos cálculos feitos anteriormente é aproveitado para
    # o interior do novo intervalo, pelo que o método exige demasiados cálculos da função f(x), não se afigurando,
    # portanto, o mais eficaz.

    # ------------ MÉTODO DA ÁUREA ------------
    # Este método vem corrigir a desvantagem do método anterior uma vez que consiste em encontrar uma divisão do intervalo
    # de tal forma que o mais baixo dos valores calculados possa ser reaproveitado na comparação seguinte, evitando, portanto,
    # a necessidade de se realizarem tantos cálculos da função f(x)

