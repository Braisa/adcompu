import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

second = lambda t, zero, first : -20.6*zero - .6*first
second_wrapped = lambda t, z : second(t, *z)

times = np.linspace(0, 10, 1000)

initial_values = [5, 0]

solution = solve_ivp(second_wrapped, (np.min(times), np.max(times)), initial_values, t_eval=times)

fig, axs = plt.subplots(2, 1, figsize=(6, 8))

axs[0].plot(solution.t, solution.y[0], ls="solid", color="tab:orange")

axs[0].set_xlim(left=np.min(times), right=np.max(times))

axs[0].set_xlabel(r"$t$")
axs[0].set_ylabel(r"$x$")

axs[1].plot(solution.t, solution.y[1], ls="solid", color="tab:purple")

axs[1].set_xlim(left=np.min(times), right=np.max(times))

axs[1].set_xlabel(r"$t$")
axs[1].set_ylabel(r"$x^\prime$")

fig.savefig("diego/day-8/second_order_derivative.pdf", bbox_inches="tight")
