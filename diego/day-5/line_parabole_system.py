import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

line_func = lambda x1, x2 : 1.4*x1 - x2 - .6
parabole_func = lambda x1, x2 : x1**2 - 1.6*x1 - x2 - 4.6
system = lambda x : (line_func(*x), parabole_func(*x))

solve_guesses = ([-1, -1.5], [4, .5])

solutions = []
for solve_guess in solve_guesses:
    solutions.append(fsolve(system, solve_guess))

print(f"As solucións (x1, x2) atopadas para o sistema son:\n{solutions}")

search_precision = 6
search_sweep = np.linspace(-10, 10, 1000)
search_solutions = []
for x1_guess in search_sweep:
    guess_solution = np.round(fsolve(system, (x1_guess, 0)), search_precision)
    if not guess_solution[0] in np.ravel(search_solutions)[::2]:
        search_solutions.append(guess_solution)

print(f"As solucións (x1, x2) atopadas para o sistema coa búsqueda amplia son:\n{solutions}")

fig, ax = plt.subplots()

xlin = np.linspace(-2, 5, 1000)

ax.plot(xlin, line_func(xlin, xlin), label=r"$x_2 = 1.4 x_1 - 0.6$")
ax.plot(xlin, parabole_func(xlin, xlin), label=r"$x_2 = x1^2 - 1.6 x_1 - 4.6$")

ax.set_xlim(left=np.min(xlin), right=np.max(xlin))

ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")

ax.legend(loc="best")

fig.savefig("diego/day-5/line_parabole_system.pdf", bbox_inches="tight")
