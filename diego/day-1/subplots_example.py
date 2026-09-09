import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1)

xs = np.linspace(0, 10, 1000)

funcs = (np.sin, np.cos)
labels = (r"$sen(x)$", r"$cos(x)$")

for (ax, func, lab) in zip(axs, funcs, labels):

    ax.plot(xs, func(xs), ls="solid", color="tab:orange")

    ax.set_xlim(left=np.min(xs), right=np.max(xs))
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(lab)


fig.savefig("diego/day-1/subplots_example.pdf")
