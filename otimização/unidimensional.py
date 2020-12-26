import math

# o método de trisecção baseia-se na constatação que,
# num intervalo contendo um mínimo e subdividido em três subintervalos,
# um dos subintervalos extremos não pode conter o mínimo sem violar a condição de unimodalidade

# definir intervalo do tipo [a, b, c, d] que contenha o mínimo da função
def trisection_method(a, b, c, d, f, iterations):
    for i in range(iterations):
        if f(b) > f(c):
            a = b
        else:
            d = c
        print("a = {} f(a) = {}\nb = {} f(b) = {}\nc = {} f(c) = {}\nd= {} f(d) = {}".format(a, f(a), b, f(b), c, f(c), d, f(d)))


# definir intervalo do tipo [a, d] que contenha o mínimo da função
def thirds_method(a, d, f, iterations):
    for i in range(iterations):
        b = a + (d - a) / 3
        c = d - (d - a) / 3
        if f(b) > f(c):
            a = b
        else:
            d = c
        print("a = {} f(a) = {}\nb = {} f(b) = {}\nc = {} f(c) = {}\nd= {} f(d) = {}".format(a, f(a), d, f(d), b, f(b), c, f(c)))


# definir intervalo do tipo [a, d] que contenha o mínimo da função
def aurea_method(a, d, f, iterations):
    B = (math.sqrt(5) - 1) / 2
    A = B ** 2
    b = A * (d - a) + a
    c = B * (d - a) + a
    for i in range(iterations):
        if f(b) < f(c):
            d = c
            c = B * (d - a) + a
        else:
            a = b
            b = A * (d - a) + a
        print("a = {} f(a) = {}\nb = {} f(b) = {}\nc = {} f(c) = {}\nd= {} f(d) = {}".format(a, f(a), d, f(d), b, f(b), c, f(c)))


