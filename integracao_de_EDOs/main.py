import runge_kutta
import euler

def df(x, y):
    return x ** 2 + y ** 2

if __name__ == '__main__':
    print(euler.euler_method(0, 0, 0.7, 0.1, df))
    print(euler.euler_qc(0, 0, 0.7, 0.1, df))
    print(euler.euler_error(0, 0, 0.7, 0.1, df))
    print()

    print(runge_kutta.rk2_method(0, 0, 0.7, 0.1, df))
    print(runge_kutta.rk2_qc(0, 0, 0.7, 0.1, df))
    print(runge_kutta.rk2_error(0, 0, 0.7, 0.1, df))
    print()

    print(runge_kutta.rk4_method(0, 0, 0.7, 0.1, df))
    print(runge_kutta.rk4_qc(0, 0, 0.7, 0.1, df))
    print(runge_kutta.rk4_error(0, 0, 0.7, 0.1, df))
    print()
