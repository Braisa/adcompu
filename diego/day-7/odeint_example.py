import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

deriv = lambda t, y : -y

initial_value = 1
times = np.linspace(0, 3, 1000)

solution = odeint(deriv, initial_value, times, tfirst=True)

fig, ax = plt.subplots()

ax.plot(times, solution, ls="solid", color="tab:orange")

ax.set_xlim(left=np.min(times), right=np.max(times))

ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$y(t)$")

fig.savefig("diego/day-7/odeint_example.pdf", bbox_inches="tight")
