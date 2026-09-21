import numpy as np
import matplotlib.pyplot as plt

func = lambda x, y : x**2 + y**4 + x + y

fig, ax = plt.subplots(subplot_kw={"projection" : "3d"})

lins = np.linspace(-5, 5, 1000)

X, Y = np.meshgrid(lins, lins)

ax.plot_wireframe(X, Y, func(X, Y), color="tab:orange")

ax.set_xlim(left=np.min(lins), right=np.max(lins))
ax.set_ylim(bottom=np.min(lins), top=np.max(lins))

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")

ax.view_init(elev=20, azim=-30, roll=0)

fig.savefig("diego/day-7/plot3d_example.pdf", bbox_inches="tight")
