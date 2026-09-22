import numpy as np
import matplotlib.pyplot as plt
from cmasher import get_sub_cmap

def wave_step(y_now, y_past, r):
    y_next = np.zeros_like(y_now)
    y_next[1:-1] = 2*y_now[1:-1] - y_past[1:-1] + r**2 * (y_now[2:] + y_now[:-2] - 2*y_now[1:-1])
    return y_now, y_next

L, timelength, c = 1, .5, 2

boundary_f = lambda x : np.sin(np.pi * x) + np.sin(2*np.pi * x)
boundary_g = lambda x : 0

dx = .04
N = 1 + int(round(L / dx))
xlin = np.linspace(0, L, N)

snapshot_times = (0, .125, .25, .375, .5)

dt = .02
timesteps = 1 + int(timelength/dt)

r = c * dt / dx

y_past = boundary_f(xlin)
y_now = np.zeros_like(y_past)

snapshot_steps = [int(round(time / dt)) for time in snapshot_times]

snapshots = {
    0.0 : y_past.copy()
}

for timestep in range(timesteps):
    y_past, y_now = wave_step(y_now, y_past, r)

    if timestep in snapshot_steps:
        snapshots[round(timestep * dt, 6)] = y_now.copy()

fig, ax = plt.subplots()

snapshot_colors = [c for c in get_sub_cmap("plasma", .2, .8, N=len(list(snapshots.keys()))).colors]
for (time, snapshot, snap_color) in zip(list(snapshots.keys()), list(snapshots.values()), snapshot_colors):
    ax.plot(xlin, snapshot, ls="solid", color=snap_color, label=f"$t = {time:.3f}$ s")

ax.set_xlim(left=np.min(xlin), right=np.max(xlin))

ax.set_xlabel(r"$x$ (m)")
ax.set_ylabel(r"$y$ (cm)")

ax.legend(loc="best")

fig.tight_layout()
fig.savefig("numerical-methods/xabier/day-2/coarse_string.pdf", bbox_inches="tight")
