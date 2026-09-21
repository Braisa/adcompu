import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "numerical-methods/diego/day-4/data0c.txt"

x, y, sy = np.loadtxt(DATA_FILE, unpack=True)

fig, ax = plt.subplots()

ax.errorbar(x, y, yerr=sy, capsize=4, color="tab:orange", fmt="o", ls=None)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

fig.savefig("numerical-methods/diego/day-4/loadtxt_uncertainties.pdf", bbox_inches="tight")
