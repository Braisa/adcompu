import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from cmasher import get_sub_cmap
from matplotlib.ticker import FixedFormatter

def get_boundary(side):
    V = np.zeros((side, side))
    boundary_mask = np.zeros_like(V, dtype=bool)
    boundary_values = np.zeros_like(V)

    boundary_mask[:,0] = True
    boundary_mask[-1,:] = True
    boundary_mask[:,-1] = True

    V[0,:] = 1
    boundary_mask[0,:] = True
    boundary_values[0,:] = V.copy()[0,:]

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

def jacobi_step(V, mask, mask_values):
    V_new = V.copy()
    V_new[1:-1, 1:-1] = .25 * (V[1:-1, :-2] + V[1:-1, 2:] + V[:-2, 1:-1] + V[2:, 1:-1])
    return V_new

tolerance = 1e-8
maximum_steps = 5000
side = 40

fig, axs = plt.subplots(1, 2, figsize=(10,4))
fig_c, axs_c = plt.subplots(1, 2, figsize=(10,4))
methods = (jacobi_step, gauss_seidel_rb_step)
titles = ("Jacobi", "Gauss-Seidel RB")

for ax, ax_c, method, title in zip(axs, axs_c, methods, titles):

    V_initial, boundary_mask, boundary_values = get_boundary(side)
    V_prev = V_initial.copy()

    for step in tqdm(range(maximum_steps)):
        V_check = V_prev.copy()
        V_step = method(V_prev, boundary_mask, boundary_values)

        below_tolerance = np.all(np.abs(V_step - V_check) < tolerance)
        if not below_tolerance:
            V_prev = V_step.copy()
        else:
            break

    cax = ax.imshow(V_step, cmap=get_sub_cmap("plasma", .2, .8))

    cs = ax_c.contour(V_step, cmap=get_sub_cmap("plasma", .2, .8))
    ax_c.clabel(cs, fontsize=10)

    for a in (ax, ax_c):
        a.set_xticks([-.5, side-.5])
        a.set_yticks([-.5, side-.5])
    
        a.set_xticklabels(["0", "40"])
        a.set_yticklabels(["0", "40"])
    
        a.set_title(f"{title}\n({step+1} steps)")

fig.colorbar(cax, ax=axs, orientation="vertical", fraction=.1, ticks=[cax.norm.vmin, cax.norm.vmax], format=FixedFormatter([r"$0$ V", r"$100$ V"]))

fig.savefig("numerical-methods/xabier/day-1/method_comparison.pdf", bbox_inches="tight")

fig_c.savefig("numerical-methods/xabier/day-1/method_comparison_contour.pdf", bbox_inches="tight")
