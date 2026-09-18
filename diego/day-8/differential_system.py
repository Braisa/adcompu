import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

systems = (
    lambda t, x, y : (x - x*y - .1*x**2, x*y - y - .05*y**2),
    lambda t, x, y : (-.1*x, .1*x - .2*y)
)

initial_values = (
    [2, 1],
    [100, 0]
)

times = (
    np.linspace(0, 30, 1000),
    np.linspace(0, 20, 1000)
)

lims = (
    (0, 2),
    (0, 100)
)

names = (
    "spiral",
    "mountain"
)

for (system, initial_value, time, lim, name) in zip(systems, initial_values, times, lims, names):

    system_wrapped = lambda t, z : system(t, *z)
    solution = solve_ivp(system_wrapped, (np.min(time), np.max(time)), initial_value, t_eval=time)

    fig, axs = plt.subplots(3, 1, figsize=(6, 10))

    labels = [
        (r"$t$", r"$x$"),
        (r"$t$", r"$y$"),
        (r"$x$", r"$y$")
    ]

    axs[0].plot(solution.t, solution.y[0], ls="solid", color="tab:orange")

    axs[0].set_xlim(left=np.min(time), right=np.max(time))

    axs[0].set_xlabel(labels[0][0])
    axs[0].set_ylabel(labels[0][1])

    axs[1].plot(solution.t, solution.y[1], ls="solid", color="tab:orange")

    axs[1].set_xlim(left=np.min(time), right=np.max(time))

    axs[1].set_xlabel(labels[1][0])
    axs[1].set_ylabel(labels[1][1])

    axs[2].plot(solution.y[0], solution.y[1], ls="solid", color="tab:purple")

    axs[2].set_xlim(left=lim[0], right=lim[1])

    axs[2].set_xlabel(labels[2][0])
    axs[2].set_ylabel(labels[2][1])

    fig.savefig(f"diego/day-8/differential_system_{name}.pdf", bbox_inches="tight")
