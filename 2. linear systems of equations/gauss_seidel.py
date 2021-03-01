# definir fórmulas de recorrência com base nas equações do sistema
# neste caso:
# 3x + y + z = 7 <=> x_formula
# x + 4y + 2z = 4 <=> y_formula
# 2y + 5z = 5 <=> z_formula

# NO MÉTODO DE GAUSS-SEIDEL só x é calculado com os valores da iteração anterior,
# no cálculo de y já se utiliza o valor de x atualizado e no cálculo de z já utiliza o valor de y atualizado

def x_formula(x, y, z):
    return (7 - y - z) / 3

def y_formula(x, y, z):
    return (4 - x - 2 * y) / 4

def z_formula(x, y, z):
    return (5 - 2 * y) / 5


def gauss_seidel_method(x, y, z):
    iterations = 0
    while True:
        iterations += 1
        xk = x
        yk = y
        zk = z
        x = x_formula(xk, yk, zk)
        y = y_formula(x, yk, zk)
        z = z_formula(x, y, zk)
        if abs(x - xk) < 1e-10 and abs(y - yk) < 1e-10 and abs(z - zk) < 1e-10:
            return x, y, z, iterations