import numpy as np
import matplotlib.pyplot as plt

def ftcs_step(T, r, step):
    T[step+1, 1:-1] = T[step, 1:-1] + r * (T[step, 2:] + T[step, :-2] - 2*T[step, 1:-1])
    return T

L, timelength, c2 = .5, .6, .049
N = 11

dx = L / (N-1)
xlin = np.linspace(0, L, N)

dts = (1e-2, 1e-1)
titles = ("Stable", "Unstable")
fig, axs = plt.subplots(1, 2, figsize=(14, 4))

for (dt, title, ax) in zip(dts, titles, axs):

    timesteps = 1 + int(timelength/dt)

    r = c2 * dt / dx**2

    T_initial = np.zeros((timesteps, N))
    T_initial[0, :] = 100

    T_step = T_initial.copy()
    for timestep in range(timesteps-1):
        T_step = ftcs_step(T_step, r, timestep)
        T_step[timestep+1, -1] = T_step[timestep+1, -2]

    ax.plot(xlin, T_initial[0, :], ls="solid", color="tab:purple", label="Initial state")
    ax.plot(xlin, T_step[-1, :], ls="solid", color="tab:orange", label="Final state")

    ax.set_xlim(left=np.min(xlin), right=np.max(xlin))

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$T$")

    ax.legend(loc="lower right")

    ax.set_title(f"{title}, r = {r:.2f}")

fig.savefig("numerical-methods/xabier/day-2/heat_insulation.pdf", bbox_inches="tight")
