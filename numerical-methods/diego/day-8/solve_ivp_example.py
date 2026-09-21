import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

derivs = (
    lambda t, y : -y,
    lambda t, x : -x**3 + np.sin(t)
)

initial_values = (
    [1],
    [0]
)

times = (
    np.linspace(0, 3, 1000),
    np.linspace(0, 10, 1000)
)

labels = (
    r"$y$",
    r"$x$"
)

names = (
    "homogeneous",
    "inhomogeneous"
)

for (deriv, initial_value, time, label, name) in zip(derivs, initial_values, times, labels, names):

    solution = solve_ivp(deriv, (np.min(time), np.max(time)), initial_value, t_eval=time)

    fig, ax = plt.subplots()

    ax.plot(solution.t, solution.y[0], ls="solid", color="tab:orange")

    ax.set_xlim(left=np.min(time), right=np.max(time))

    ax.set_xlabel(r"$t$")
    ax.set_ylabel(label)

    fig.savefig(f"diego/day-8/solve_ivp_example_{name}.pdf", bbox_inches="tight")
