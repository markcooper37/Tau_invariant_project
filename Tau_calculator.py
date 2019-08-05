# Tau calculator

import numpy as np
def generalized_inverse(L):
    j = np.ones(np.size(L, 0))
    v = np.size(L, 0)
    j_adjusted = np.true_divide(j, v)
    return np.linalg.inv(L - j_adjusted) + j_adjusted


def tau_calculator(L):
    L_plus = generalized_inverse(L)
    v = np.size(L, 0)
    tau_1 = 0
    tau_2 = 0
    trace_L_plus = np.trace(L_plus)
    for i in range(0, v):
        for j in range(i + 1, v):
            if L[i, j] != 0:
                tau_1 = tau_1 - L[i, j] * ((1 / L[i, j]) + L_plus[i, i] - (2 * L_plus[i, j]) + L_plus[j, j])**2
                tau_2 = tau_2 - L[i, j] * (L_plus[i, i] - L_plus[j, j])**2
    return (tau_1 / 12) + (tau_2 / 4) + (trace_L_plus / v)


def tau_ratio(L):
    length = 0
    v = np.size(L, 0)
    for i in range(0, v):
        for j in range(i + 1, v):
            if L[i, j] != 0:
                length = length - (1 / L[i, j])
    tau = tau_calculator(L)
    return tau / length


a = np.array([[18, -6, -6, -6], [-6, 18, -6, -6], [-6, -6, 18, -6], [-6, -6, -6, 18]])
print(tau_ratio(a))

b = np.array([[4, -4, 0, 0, 0], [-4, 12, -4, -4, 0], [0, -4, 4, 0, 0], [0, -4, 0, 8, -4], [0, 0, 0, -4, 4]])
c = np.array([[10, -5, -5, 0], [-5, 15, -5, -5], [-5, -5, 15, -5], [0, -5, -5, 10]])

print(tau_ratio(b))
print(tau_ratio(c))

