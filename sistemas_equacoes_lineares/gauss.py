from copy import deepcopy

def invert_matrix(M):
    temp = deepcopy(M)
    i = 0
    j = 0
    for line in reversed(range(len(M))):
        for col in reversed(range(len(M[0]))):  # there are columns to deal with
            temp[i][j] = M[line][col]
            j += 1
        i += 1
        j = 0
    M = temp
    return M


def gaussian_elimination(M, X):
    changed_X = False
    for i in range(len(M)):
        pivot = M[i][i]
        if pivot == 0: return "pivot can not be 0"
        for k in range(i, len(M[0])):
            M[i][k] /= pivot
        X[i][0] /= pivot
        for j in range(i + 1, len(M)):
            factor = (-M[j][i])
            for k in range(i, len(M[0])):
                M[j][k] += factor * M[i][k]
                if not changed_X:
                    X[j][0] += factor * X[i][0]
                    changed_X = True
            changed_X = False
    return M, X


def gauss_method(M, X):
    M, X = gaussian_elimination(M, X)
    M = invert_matrix(M)
    X = invert_matrix(X)
    M, X = gaussian_elimination(M, X)
    X = invert_matrix(X)
    return X
