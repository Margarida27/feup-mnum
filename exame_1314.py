import math as m


# EX 1
def rec(x): return (4*x**3-x+1)**(1/4)
def picard_peano(x):
    for i in range(3):
        print(x)
        x = rec(x)


# EX 2
# NO MAXIMA
# A:matrix([0.1,0.5,3.0,0.25],[1.2,0.2,0.25,0.2],[-1.0,0.25,0.3,2.0],[2.0,0.00001,1.0,0.4]);
# B:matrix([0.0],[1.0],[2.0],[3.0]);
# M:addcol(A,B);
# M:float(echelon(M));
# M:rowop(M,1,2,M[1][2]);
# M:rowop(M,1,3,M[1][3]);
# M:rowop(M,1,4,M[1][4]);
# M:rowop(M,2,3,M[2][3]);
# M:rowop(M,2,4,M[2][4]);
# M:rowop(M,3,4,M[3][4]);
# X:matrix([M[1][5]],[M[2][5]],[M[3][5]],[M[4][5]]);
# da:matrix([0.3],[0.3],[0.3],[0.3]);
# db:matrix([0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3]);
# dx:invert(A).(da-db.X);


# EX 3
def dx(t,x,v,k): return v
def dv(t,x,v,k): return (-v-k*x)/20
def euler(t0,x0,v0,k,h):
    while t0 <= 5.0 + h:
        print(t0,x0)
        v0 += h*dv(t0,x0,v0,k)
        x0 += h*dx(t0,x0,v0,k)
        t0 += h


# EX 6
def f(x): return x + ((x-2)**2)/(m.sin(x)+4)
def aurea(x1,x2):
    B = (m.sqrt(5)-1)/2
    A = B**2
    for i in range(3):
        x3 = A*(x2-x1)+x1
        x4 = B*(x2-x1)+x1
        print(x1,x2,x3,x4,f(x1),f(x2),f(x3),f(x4))
        if f(x3) < f(x4):
            x2 = x4
        else:
            x1 = x3


if __name__ == '__main__':
    
    # EX 1
    # picard_peano(4.0)

    # EX 3
    # euler(0,1,0,5,0.2)
    # observando os valores das iterações do método de euler
    # conclui-se que k=5 produz os valores mais próximos aos do gráfico

    # EX 4
    # definindo certos valores para m e R, por exemplo, m = 2 e R = 10
    # verifica-se que a derivada da fórmula b é 0 a partir de certos valores de x
    # portanto esta fórmula não pode ser utilizada na aplicação do método

    # EX 6
    # aurea(-1.0,1.5)
    # a amplitude do intervalo é dada por x4-x1
    # há que observar os valores de f obtidos na última iteração
    # e, assim, concluir qual o subintervalo que será excluído
    # neste caso seria excluído o subintervalo [x4,x2], porque aí f volta a crescer
    # e, portanto, o próximo intervalo a considerar seria [x1,x3,x4]