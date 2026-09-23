import numpy as np
from matplotlib.pyplot import subplots
from tqdm import tqdm
from cmasher import get_sub_cmap
from matplotlib.ticker import FixedFormatter
from matplotlib.colors import Normalize, LogNorm
from matplotlib.colorizer import Colorizer

def get_boundary(side):
    V = np.zeros((side, side))
    boundary_mask = np.zeros_like(V, dtype=bool)
    boundary_values = np.zeros_like(V)

    boundary_mask[:,0] = True
    boundary_mask[:,-1] = True

    V[0,:] = +100
    boundary_mask[0,:] = True
    boundary_values[0,:] = V.copy()[0,:]

    V[-1,:] = -100
    boundary_mask[-1,:] = True
    boundary_values[-1,:] = V.copy()[-1,:]

    return V, boundary_mask, boundary_values

def gauss_seidel_rb_step(V, mask, mask_values):
    V[1:-1:2,1:-1:2] = 0.25*(
        V[:-2:2,1:-1:2] + V[2::2,1:-1:2] +
        V[1:-1:2,:-2:2] + V[1:-1:2,2::2]
    )
    V[2:-1:2,2:-1:2] = 0.25*(
        V[1:-2:2,2:-1:2] + V[3::2,2:-1:2] +
        V[2:-1:2,1:-2:2] + V[2:-1:2,3::2]
    )

    V[2:-1:2,1:-1:2] = 0.25*(
        V[1:-2:2,1:-1:2] + V[3::2,1:-1:2] +
        V[2:-1:2,:-2:2] + V[2:-1:2,2::2]
    )
    V[1:-1:2,2:-1:2] = 0.25*(
        V[:-2:2,2:-1:2] + V[2::2,2:-1:2] +
        V[1:-1:2,1:-2:2] + V[1:-1:2,3::2]
    )

    V[mask] = mask_values[mask]
    return V

tolerance = 1e-12
maximum_steps = 5000
side = 40

fig, ax = subplots()

norm = Normalize(vmin=-100, vmax=+100)
colorizer = Colorizer(norm=norm, cmap=get_sub_cmap("viridis", .2, .8))

V_initial, boundary_mask, boundary_values = get_boundary(side)
V_prev = V_initial.copy()

for step in tqdm(range(maximum_steps)):
    V_check = V_prev.copy()
    V_step = gauss_seidel_rb_step(V_prev, boundary_mask, boundary_values)

    below_tolerance = np.all(np.abs(V_step - V_check) < tolerance)
    if not below_tolerance:
        V_prev = V_step.copy()
    else:
        break

cax = ax.imshow(V_step, colorizer=colorizer)

ax.set_xticks([-.5, side-.5])
ax.set_yticks([-.5, side-.5])

ax.set_xticklabels(["0", "40"])
ax.set_yticklabels(["0", "40"])

fig.colorbar(cax, ax=ax, location="right", orientation="vertical", fraction=.1, ticks=[norm.vmin, norm.vmax], format=FixedFormatter([r"$-100$ V", r"$+100$ V"]))

fig.tight_layout()
fig.savefig("numerical-methods/xabier/extras/simple_laplace.pdf", bbox_inches="tight")
