import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "diego/day-3/data2s.txt"

data = np.loadtxt(DATA_FILE)
x, y = data.T

fig, ax = plt.subplots()

ax.plot(x, y, "o", color="tab:orange")

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

fig.savefig("diego/day-3/loadtxt_example.pdf", bbox_inches="tight")
