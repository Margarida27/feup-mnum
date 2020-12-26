# 1. representar a função no Maxima
# 2. verificar o número de raizes
# 3. isolar cada uma das raizes e definir guesses
# 4. escolher critério de paragem
# 5. implementar o método


#critério de precisão absoluta
#consiste em parar quando o intervalo que contêm a raiz for menor que um dado valor, e
def bissection_absolute_precision(a, b, e, f):
    while abs(a - b) > e:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m


#critério de precisão relativa
#consiste em parar quando a razão entre o intervalo que contêm a raiz e a própria raiz for menor do que um dado valor, e
def bissection_relative_precision(a, b, e, f):
    while abs((a - b) / a) > e or abs((a - b) / b) > e:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m


#critério da anulação da função
#consiste em parar quando a diferença entre o valor da função nos extremos do intervalo que contêm a raiz for menor que um dado valor, e
def bissection_func_annulment(a, b, e, f):
    while abs(f(a) - f(b)) > e:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m


#critério do número de iterações
#consiste em parar quando tiverem, sido feitas n iterações
def bissection_num_iterations(a, b, n, f):
    for i in range(n):
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m
