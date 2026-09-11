import numpy as np
import matplotlib.pyplot as plt

eq_a = lambda x : .5 * (x - 1)
eq_b = lambda x : .5 * (11 - 3*x)

xs = np.linspace(-5, 5, 100)

fig, ax = plt.subplots()

ax.plot(xs, eq_a(xs), ls="solid", color="tab:purple")
ax.plot(xs, eq_b(xs), ls="solid", color="tab:orange")

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

ax.set_xlim(left=np.min(xs), right=np.max(xs))

ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(.25))

fig.savefig("diego/day-3/visual_equation_system.pdf", bbox_inches="tight")
