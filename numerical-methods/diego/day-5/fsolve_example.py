import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

cos_func = lambda x, a, b : x + b * np.cos(x) - a

A, B = 4, 2
solve_guess = 4

solution = fsolve(cos_func, solve_guess, args=(A, B))

print(f"A solución a x + 2cos x - 4 = 0 atópase en x = {solution[0]:.4f}")

fig, ax = plt.subplots()

xlin = 5 * np.linspace(-1, 1, 1000)
ybot, ytop = -10, 3

ax.hlines(0, xmin=np.min(xlin), xmax=np.max(xlin), ls="dashed", color="tab:gray")
ax.vlines(solution, ymin=ybot, ymax=ytop, ls="dashed", color="tab:purple")
ax.plot(xlin, cos_func(xlin, A, B), ls="solid", color="tab:orange")

ax.set_xlim(left=np.min(xlin), right=np.max(xlin))
ax.set_ylim(bottom=ybot, top=ytop)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$x + 2\cos x - 4$")

fig.savefig("diego/day-5/fsolve_example.pdf", bbox_inches="tight")
