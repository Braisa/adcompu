import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

third = lambda t, zero, first, second : -np.exp(-t) - 60*t*np.sin(t)**2 - 40*t**3*np.cos(t)**2
third_wrapped = lambda t, z : third(t, *z)

times = np.linspace(0, 6, 1000)

initial_values = [0, -1, 11]

solution = solve_ivp(third_wrapped, (np.min(times), np.max(times)), initial_values, t_eval=times)

fig, axs = plt.subplots(3, 1, figsize=(6, 12))

colors = ("tab:orange", "tab:purple", "tab:blue")
labels = (r"$x$", r"$x^\prime$", r"x$^{\prime\prime}$")

for (ax, sol, col, lab) in zip(axs, solution.y, colors, labels):

    ax.plot(solution.t, sol, ls="solid", color=col)

    ax.set_xlim(left=np.min(times), right=np.max(times))

    ax.set_xlabel(r"$t$")
    ax.set_ylabel(lab)

    ins = ax.inset_axes([0.1, 0.1, .4, .6], xlim=(0, 1), ylim=(-2, 13))

    ins.plot(solution.t, sol, ls="solid", color=col)

    ax.indicate_inset_zoom(ins, edgecolor="black")

fig.savefig("numerical-methods/diego/day-8/third_order_derivative.pdf", bbox_inches="tight")
