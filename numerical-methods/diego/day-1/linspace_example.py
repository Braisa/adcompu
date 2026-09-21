import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

xs = np.linspace(1, 3, 15)
ys = xs**2 * np.exp(-xs**2)

ax.plot(xs, ys, "o", color="tab:red")

ax.set_xlabel(r"$x_i$")
ax.set_ylabel(r"$y_i$")

ax.grid(True) # -_-

fig.savefig("diego/linspace_example.pdf", bbox_inches="tight")
