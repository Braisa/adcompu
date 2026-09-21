import numpy as np
import matplotlib.pyplot as plt
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
    boundary_mask[0,:] = True
    boundary_mask[:,-1] = True

    V[-1,:] = np.sin(np.pi * np.linspace(0, 1, side))
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

tolerance = 1e-8
maximum_steps = 15_000

sides = (10, 20, 40, 80, 120)
fig, axs = plt.subplots(3, len(sides), figsize=(20, 8))
maximum_errors = np.zeros_like(sides, dtype=np.float64)

vir_norm = Normalize(vmin=0, vmax=1)
vir_colorizer = Colorizer(norm=vir_norm, cmap=get_sub_cmap("viridis", .2, .8))

pla_norm = LogNorm(vmin=1e-6, vmax=1e-2)
pla_colorizer = Colorizer(norm=pla_norm, cmap=get_sub_cmap("plasma", .2, .8))

for i, side in enumerate(sides):

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

    side_values = np.linspace(0, 1, side)
    grid_values_x, grid_values_y = np.meshgrid(side_values, side_values)

    V_exact = exact(grid_values_x, grid_values_y)
    V_exact[boundary_mask] = boundary_values[boundary_mask]
    V_error = np.abs(V_step[1:-1,1:-1] - V_exact[1:-1,1:-1])
    maximum_errors[i] = np.max(V_error)

    numerical_ax = axs[0,i]
    vcax = numerical_ax.imshow(V_step, colorizer=vir_colorizer)
    if i == 0: numerical_ax.set_ylabel("Numerical solution")

    difference_ax = axs[1,i]
    pcax = difference_ax.imshow(np.abs(V_step - V_exact), colorizer=pla_colorizer)
    if i == 0: difference_ax.set_ylabel("Difference")

    exact_ax = axs[2,i]
    exact_ax.imshow(V_exact, colorizer=vir_colorizer)
    if i == 0: exact_ax.set_ylabel("Exact solution")

    for ax in (numerical_ax, exact_ax, difference_ax):
        ax.set_xticks([-.5, side-.5])
        ax.set_yticks([-.5, side-.5])
    
        ax.set_xticklabels(["0", "1"])
        ax.set_yticklabels(["0", "1"])

fig.colorbar(vcax, ax=axs, location="right", orientation="vertical", fraction=.1, ticks=[vir_norm.vmin, vir_norm.vmax], format=FixedFormatter([r"$0$", r"$1$"]))

fig.colorbar(pcax, ax=axs, location="right", orientation="vertical", fraction=.1, ticks=[pla_norm.vmin, pla_norm.vmax], format=FixedFormatter([f"${pla_norm.vmin:.2E}$", f"${pla_norm.vmax:.2E}$"]))

fig.savefig("numerical-methods/xabier/day-1/gauss_seidel.pdf", bbox_inches="tight")

fig, ax = plt.subplots()

ax.bar(sides, maximum_errors, color="tab:orange")

ax.set_yscale("log")

ax.set_xticks(sides)

ax.set_xlabel("Grid side")
ax.set_ylabel("Maximum absolute error")

fig.savefig("numerical-methods/xabier/day-1/gauss_seidel_errors.pdf", bbox_inches="tight")
