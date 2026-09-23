import numpy as np
from matplotlib.pyplot import subplots
from tqdm import tqdm
from cmasher import get_sub_cmap
from matplotlib.ticker import FixedFormatter
from matplotlib.colors import Normalize, LogNorm
from matplotlib.colorizer import Colorizer
from matplotlib.patches import Rectangle

def jacobi_step(V):
    V_new = V.copy()
    V_new[1:-1, 1:-1] = .25 * (V[1:-1, :-2] + V[1:-1, 2:] + V[:-2, 1:-1] + V[2:, 1:-1])
    return V_new

length = 100
rho = 1e-4
extension = 20

tolerance = 1e-12
maximum_steps = 20_000
side = 200

h = length/side
eps = 8.854e-14

fig, axs = subplots(1, 2, figsize=(16, 6))

norm = Normalize(vmin=-rho*h**2/eps, vmax=+rho*h**2/eps)
colorizer = Colorizer(norm=norm, cmap=get_sub_cmap("plasma", .2, .8))

rho_matrix_neg = np.zeros((side, side))
rho_matrix_neg[int(.6*side):int(.8*side), int(.2*side):int(.4*side)] = -rho

rho_matrix_both = rho_matrix_neg.copy()
rho_matrix_both[int(.2*side):int(.4*side), int(.6*side):int(.8*side)] = rho

rho_matrices = (rho_matrix_neg, rho_matrix_both)

neg_rect = Rectangle((int(.2*side), int(.6*side)), int(.2*side), int(.2*side), fc=get_sub_cmap("plasma", .1, .8).colors[0], hatch="x", ec="tab:blue")

neg_rect2 = Rectangle((int(.2*side), int(.6*side)), int(.2*side), int(.2*side), fc=get_sub_cmap("plasma", .1, .8).colors[0], hatch="x", ec="tab:blue")
pos_rect = Rectangle((int(.6*side), int(.2*side)), int(.2*side), int(.2*side), fc=get_sub_cmap("plasma", .2, .9).colors[-1], hatch="x", ec="tab:red")

rects_col = [[neg_rect], [neg_rect2, pos_rect]]

for rho_matrix, ax, rects in zip(rho_matrices, axs, rects_col):

    V_initial = np.zeros((side, side))
    V_prev = V_initial.copy()

    for step in tqdm(range(maximum_steps)):
        V_step = jacobi_step(V_prev)
        V_step[1:-1] += h**2/4/eps * rho_matrix[1:-1]

        below_tolerance = np.all(np.abs(V_step - V_prev) < tolerance)
        if not below_tolerance:
            V_prev = V_step.copy()
        else:
            break

    cax = ax.imshow(V_step, colorizer=colorizer)

    for rect in rects:
        ax.add_patch(rect)

    ax.set_xticks([-.5, side-.5])
    ax.set_yticks([-.5, side-.5])

    ax.set_xticklabels(["0", f"{side}"])
    ax.set_yticklabels(["0", f"{side}"])

fig.colorbar(cax, ax=axs, location="right", orientation="vertical", fraction=.1, ticks=[norm.vmin, norm.vmax], format=FixedFormatter([r"$-100$ V", r"$+100$ V"]))

fig.savefig("numerical-methods/xabier/extras/poisson.pdf", bbox_inches="tight")
