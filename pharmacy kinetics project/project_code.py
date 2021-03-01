import math
import matplotlib.pyplot as plt

PRECISION = 1e-10

# useful data about Mylmet
Ket = 0.00178333  # min ^ -1
tmax = 150  # min
Vap = 3150  # mL
dosage = 1000  # mg de 720 min em 720 min (12h em 12h)
dosage_period = 720  # min
dosage_at_tmax = 2.77777778  # mg
daily_dosage = 2000  # mg
treatment_duration = 8  # meses


# equations to find the value of Ka
def f(x): return x * math.exp(-x * tmax) - Ket * math.exp(-Ket * tmax)
def der_f(x): return math.exp(-tmax * x) - tmax * x * math.exp(-tmax * x)


# newton's method to compute the value of Ka, using absolute precision criterion (1e-10)
def newton_abs_precision(guess):
    x = guess
    xk = x - f(x) / der_f(x)
    iterations = 1
    while abs(x - xk) > PRECISION:
        x = xk
        xk = x - f(x) / der_f(x)
        iterations += 1
    return x


# Ka value obtained by applying newton's method
Ka = newton_abs_precision(0.001500000)


# implementation of D(t) - temporal function of administration
def D(t):
    if math.fmod(t, dosage_period) <= tmax:
        m = dosage_at_tmax / tmax
        t = math.fmod(t, dosage_period)
        return m * t
    else:
        m = - dosage_at_tmax / (dosage_period - tmax)
        b = dosage_at_tmax - m * tmax
        t = math.fmod(t, dosage_period)
    return m * t + b


# EDOs
def dmi_dt(t, mi): return D(t) - Ka * mi
def dmp_dt(t, mi, mp): return Ka * mi - Ket * mp
def dcp_dt(t, mi, mp): return (Ka * mi - Ket * mp) / Vap


# runge-kutta's 4th order method to solve the EDOs above
def rk4(mi_0, mp_0, t_0, t_f, h):
    mi = mi_0
    mp = mp_0
    cp = mp_0 / Vap
    t = t_0

    values_t = [t]  # x axis values
    values_cp = [cp]  # y axis values

    while abs(t_f - t) > PRECISION:
        delta1_mi = h * dmi_dt(t, mi)
        delta1_mp = h * dmp_dt(t, mi, mp)
        delta1_cp = h * dcp_dt(t, mi, mp)

        delta2_mi = h * dmi_dt(t + h / 2, mi + delta1_mi / 2)
        delta2_mp = h * dmp_dt(t + h / 2, mi + delta1_mi / 2, mp + delta1_mp / 2)
        delta2_cp = h * dcp_dt(t + h / 2, mi + delta1_mi / 2, mp + delta1_mp / 2)

        delta3_mi = h * dmi_dt(t + h / 2, mi + delta2_mi / 2)
        delta3_mp = h * dmp_dt(t + h / 2, mi + delta2_mi / 2, mp + delta2_mp / 2)
        delta3_cp = h * dcp_dt(t + h / 2, mi + delta2_mi / 2, mp + delta2_mp / 2)

        delta4_mi = h * dmi_dt(t + h, mi + delta3_mi)
        delta4_mp = h * dmp_dt(t + h, mi + delta3_mi, mp + delta3_mp)
        delta4_cp = h * dcp_dt(t + h, mi + delta3_mi, mp + delta3_mp)

        delta_mi = (delta1_mi / 6 + delta2_mi / 3 + delta3_mi / 3 + delta4_mi / 6)
        delta_mp = (delta1_mp / 6 + delta2_mp / 3 + delta3_mp / 3 + delta4_mp / 6)
        delta_cp = (delta1_cp / 6 + delta2_cp / 3 + delta3_cp / 3 + delta4_cp / 6)

        mi += delta_mi
        mp += delta_mp
        cp += delta_cp
        t += h

        values_t.append(t)
        values_cp.append(cp)

    return [values_t, values_cp]


if __name__ == '__main__':
    mi_0 = 0.0
    mp_0 = 0.0
    t_0 = 0.0
    t_f = 1440  # 1 day
    h = 1  # increments of 1 minute
    values_t = rk4(mi_0, mp_0, t_0, t_f, h)[0]
    values_cp = rk4(mi_0, mp_0, t_0, t_f, h)[1]
    plt.plot(values_t, values_cp)
    plt.suptitle('comportamento temporal da concentração de Mylmet no plasma sanguíneo durante 1 dia')
    plt.xlabel('t (min)')
    plt.ylabel('Cp (mg/mL)')
    plt.show()
