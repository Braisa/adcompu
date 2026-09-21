import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

line_func = lambda x1, x2 : 3*x1 + x2 - 1
cubic_func = lambda x1, x2 : 1.2*x1**3 - x1**2 + x2
system = lambda x : (line_func(*x), cubic_func(*x))

search_precision = 6
search_sweep = np.linspace(-3, 3, 1000)
search_solutions = []
for x1_guess in search_sweep:
    guess_solution = np.round(fsolve(system, (x1_guess, 0)), search_precision)
    if not guess_solution[0] in np.ravel(search_solutions)[::2]:
        search_solutions.append(guess_solution)

print(f"As solucións do sistema con -3 <= x1 <= 3 atopadas son:")
for solution in search_solutions:
    print(f"x1 = {solution[0]}, x2 = {solution[1]}")

fig, ax = plt.subplots()

ax.plot(search_sweep, line_func(search_sweep, 0), label=r"$x_2 = 3x_1 - 1$")
ax.plot(search_sweep, cubic_func(search_sweep, 0), label=r"$x_2 = 1.2x_1^3 - x_1^2$")

ax.set_xlim(left=np.min(search_sweep), right=np.max(search_sweep))

ax.set_xlabel(r"$x_1$")
ax.set_xlabel(r"$x_2$")

ax.legend(loc="best")

fig.savefig("numerical-methods/diego/day-5/line_cubic_system.pdf", bbox_inches="tight")
