# sendo o domínio de integração aABb um rectângulo de lados paralelos aos eixos,
# partamo-lo em quatro partes iguais pelas medianas dos lados
# e calculemos os integral interior pela regra dos Trapézios ou pela regra de Simpson

# se o rectângulo de integração é grande, a divisão a meio não chega,
# de modo que o domínio é divido em m x n rectângulos, a cada um dos quais se aplica a fórmula anterior

# se o domínio de integração não é rectangular,
# considera-se o menor rectângulo que o contém e aplica-se o mesmo método fazendo f = 0 fora do domínio

def cubatura_trapeze_method(a, A, b, B, f):
    hx = (A - a) / 2
    hy = (B - b) / 2

    # soma dos valores de f nos vértices da malha
    e0 = f(a, b) + f(a, B) + f(A, b) + f(A, B)

    # soma dos valores de f nos pontos médios dos lados da malha
    e1 = f(a + hx, b) + f(A, b + hy) + f(a + hx, B) + f(a, b + hy)

    # valor de f no centro da malha
    e2 = f(a + hx, b + hy)

    s = (hx * hy) / 4 * (e0 + 2 * e1 + 4 * e2)
    return s

def cubatura_simpson_method(a, A, b, B, f):
    hx = (A - a) / 2
    hy = (B - b) / 2

    # soma dos valores de f nos vértices da malha
    e0 = f(a, b) + f(a, B) + f(A, b) + f(A, B)

    # soma dos valores de f nos pontos médios dos lados da malha
    e1 = f(a + hx, b) + f(A, b + hy) + f(a + hx, B) + f(a, b + hy)

    # valor de f no centro da malha
    e2 = f(a + hx, b + hy)

    s = (hx * hy) / 9 * (e0 + 4 * e1 + 16 * e2)
    return s
