import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "numerical-methods/diego/day-3/data2s.txt"

x, y = np.loadtxt(DATA_FILE, unpack=True)

fig, ax = plt.subplots()

ax.plot(x, y, "o", color="tab:orange")

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

fig.savefig("numerical-methods/diego/day-3/loadtxt_example.pdf", bbox_inches="tight")
