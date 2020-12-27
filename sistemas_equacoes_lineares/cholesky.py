# NO MAXIMA: RESOLVER O SISTEMA A.x = b
# 1) [P,L,U] : get_lu_factors(lu_factor(transpose(A)))
# 2) B : transpose(L) -> matriz triangular inferior
# 3) C : transpose(U) -> matriz triangular superior
# 4) y : invert(B).matrix(b)
# 5) x : invert(C).y -> solução final


def get_L_and_U(M):
    L = [[0 for row in range(len(M[0]))] for col in range(len(M))]
    U = [[0 for row in range(len(M[0]))] for col in range(len(M))]

    for i in range(len(U)):
        U[i][i] = 1
        L[i][0] = M[i][0]

    for j in range(len(M)):
        U[0][j] = M[0][j] / L[0][0]

    for i in range(len(M)):  # for each column of L we need to calculate a row of U
        for j in range(len(M[0])):
            if i >= j:
                L[i][j] = M[i][j]
                for k in range(j):
                    L[i][j] -= L[i][k] * U[k][j]
            if i < j:
                U[i][j] = M[i][j]
                for k in range(i):
                    U[i][j] -= L[i][k] * U[k][j]
                U[i][j] /= L[i][i]

    return L, U

# returns only L and U because after having these two calculated, is easy to calculate the final solution, e.g. using Maxima
def cholesky_method(matrix):
    L, U = get_L_and_U(matrix)
    return L, U
