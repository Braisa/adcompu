import numpy as np
import matplotlib.pyplot as plt
from cmasher import get_sub_cmap
from tqdm import tqdm
from matplotlib.ticker import FixedFormatter

def jacobi_step(V):
    V_new = V.copy()
    V_new[1:-1, 1:-1] = .25 * (V[1:-1, :-2] + V[1:-1, 2:] + V[:-2, 1:-1] + V[2:, 1:-1])
    return V_new

maximum_steps = 50
tolerance = 1e-5

side = 5
V_initial = np.zeros((side, side))
V_initial[0,:] = 1

V_prev = V_initial

for step in tqdm(range(maximum_steps)):

    V_step = jacobi_step(V_prev)

    below_tolerance = np.all(np.abs(V_step - V_prev) < tolerance)
    if not below_tolerance:
        V_prev = V_step
    else:
        break

fig, ax = plt.subplots()

cax = ax.imshow(V_step, cmap=get_sub_cmap("viridis", .2, .8))

ax.set_xticks(np.arange(side))
ax.set_yticks(np.arange(side))

ax.set_xticklabels(np.arange(side))
ax.set_yticklabels(np.arange(side))

fig.colorbar(cax, ax=ax, location="right", orientation="vertical", fraction=.1, ticks=[cax.norm.vmin, cax.norm.vmax], format=FixedFormatter([r"$0$ V", r"$100$ V"]))

fig.savefig("numerical-methods/xabier/day-1/jacobi_relaxation.pdf", bbox_inches="tight")
