import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

mag_func = lambda m, C, T : m - np.tanh(C*m/T)

c = 1
solve_guess = 1

Tlin = np.linspace(1e-5, 2, 1000)
ms = np.zeros_like(Tlin)
for t, T in enumerate(Tlin):
    ms[t] = fsolve(mag_func, solve_guess, args=(c, T))[0]

fig, ax = plt.subplots()

ax.plot(Tlin, ms, ls="solid", color="tab:orange")

ax.set_xlim(left=np.min(Tlin), right=np.max(Tlin))

ax.set_xlabel(r"$T$ (K)")
ax.set_ylabel(r"$m$")

fig.savefig("diego/day-5/fsolve_mag.pdf", bbox_inches="tight")
