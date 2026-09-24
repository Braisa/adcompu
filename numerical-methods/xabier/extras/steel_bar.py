import numpy as np
from matplotlib.pyplot import subplots
from cmasher import get_sub_cmap
from matplotlib.colors import BoundaryNorm
from matplotlib.colorizer import Colorizer, ColorizingArtist

def ftcs_step(T, r, step):
    T[step+1, 1:-1] = T[step, 1:-1] + r * (T[step, 2:] + T[step, :-2] - 2*T[step, 1:-1])
    return T

length = 50
conductivity = .12
specific_heat = .113
density = 7.8
timelength = 1

dx = 5
N = 1 + int(length/dx)
xlin = np.linspace(0, length, N)

dt = .02
timesteps = 1 + int(timelength/dt)

r = (conductivity/specific_heat/density) * dt*3600 / dx**2

T_initial = np.zeros((timesteps, N))
T_initial[0, :] = 100

T_step = T_initial.copy()
for timestep in range(timesteps-1):
    T_step = ftcs_step(T_step, r, timestep)
    T_step[timestep+1, 0], T_step[timestep+1, -1] = 0, 0

fig, ax = subplots()

ts = np.arange(timesteps)[::5]
cmap = get_sub_cmap("plasma", .2, .8, N=len(ts))
for t, c in zip(ts, cmap.colors):
    ax.plot(xlin, T_step[t, :], ls="solid", color=c)

ax.set_xlim(left=np.min(xlin), right=np.max(xlin))

ax.set_ylim(bottom=0)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$T$")

bounds = ts*dt
norm = BoundaryNorm(bounds, cmap.N)
colorizer = Colorizer(norm=norm, cmap=cmap)

fig.colorbar(ColorizingArtist(colorizer), ax=ax, orientation="vertical", location="right", label=r"$t$ (h)")

fig.savefig("numerical-methods/xabier/extras/steel_bar.pdf", bbox_inches="tight")
