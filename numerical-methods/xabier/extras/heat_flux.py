import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from cmasher import get_sub_cmap
from matplotlib.ticker import FixedFormatter
from matplotlib.colors import Normalize
from matplotlib.colorizer import Colorizer

def get_boundary(side):
    V = np.zeros((side, side))
    boundary_mask = np.zeros_like(V, dtype=bool)
    boundary_values = np.zeros_like(V)

    V[:,0] = 75
    boundary_mask[:,0] = True
    boundary_values[:,0] = V.copy()[:,0]

    V[:,-1] = 50
    boundary_mask[:,-1] = True
    boundary_values[:,-1] = V.copy()[:,-1]

    V[0,:] = 100
    boundary_mask[0,:] = True
    boundary_values[0,:] = V.copy()[0,:]

    V[-1,:] = 0
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

exact = lambda x, y : np.sin(np.pi*x) * np.sinh(np.pi*y) / np.sinh(np.pi)

tolerance = 1e-12
maximum_steps = 5_000

side = 10
conductivity = .49
length = 40
h = length / side

fig, axs = plt.subplots(1, 2, figsize=(16, 6))

norm = Normalize(vmin=0, vmax=100)
colorizer = Colorizer(norm=norm, cmap=get_sub_cmap("plasma", .2, .8))


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

flux_x, flux_y = np.zeros_like(V_initial), np.zeros_like(V_initial)

flux_x[1:-1, 1:-1] = -conductivity/2/h * (V_step[1:-1, 2:] - V_step[1:-1, :-2])
flux_y[1:-1, 1:-1] = -conductivity/2/h * (V_step[2:, 1:-1] - V_step[:-2, 1:-1])

cax = axs[0].imshow(V_step, colorizer=colorizer)

axs[1].quiver(flux_x, -flux_y)
axs[1].yaxis.set_inverted(True)

for ax in axs:
    ax.set_xticks([-.5, side-.5])
    ax.set_yticks([-.5, side-.5])

    ax.set_xticklabels(["0", "1"])
    ax.set_yticklabels(["0", "1"])

fig.colorbar(cax, ax=axs, location="left", orientation="vertical", fraction=.1, ticks=[norm.vmin, norm.vmax], format=FixedFormatter([f"${norm.vmin}$ ºC", f"${norm.vmax}$ ºC"]))

fig.savefig("numerical-methods/xabier/extras/heat_flux.pdf", bbox_inches="tight")
