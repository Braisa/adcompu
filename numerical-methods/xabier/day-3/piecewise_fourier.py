import numpy as np
from matplotlib.pyplot import subplots
from scipy.integrate import quad
from cmasher import get_sub_cmap

sample_size = 2000
period = 5

piecewise_func = lambda x : (
    (x - 5) * np.heaviside(x - 5, 1) * np.heaviside(7 - x, 0)
    + 2 * np.heaviside(x - 7, 1) * np.heaviside(9 - x, 0)
    + (10 - x) * np.heaviside(x - 9, 1) * np.heaviside(10 - x, 0)
)

definition_interval = np.linspace(5, 10, sample_size)
extension_interval = np.linspace(-5, 15, sample_size)

interval_mapping = lambda x, original, target : ((x + np.min(target) - np.min(original)) % period) + np.min(target)

fig_ex, ax_ex = subplots()

ax_ex.plot(definition_interval, piecewise_func(definition_interval), ls="solid", color="tab:purple", label="Original")
ax_ex.plot(extension_interval, piecewise_func(interval_mapping(extension_interval, extension_interval, definition_interval)), ls="dashed", color="tab:orange", label="Extension")

ax_ex.axvline(np.min(definition_interval), ls="dashed", color="tab:gray")
ax_ex.axvline(np.max(definition_interval), ls="dashed", color="tab:gray")

ax_ex.set_xlim(left=np.min(extension_interval), right=np.max(extension_interval))

ax_ex.set_xlabel(r"$x$")

ax_ex.legend(loc="best")

fig_ex.tight_layout()
fig_ex.savefig("numerical-methods/xabier/day-3/piecewise_fourier_extension.pdf", bbox_inches="tight")

a_0 = 2/period * quad(piecewise_func, np.min(definition_interval), np.max(definition_interval))[0]

a_n_func = lambda x, n : piecewise_func(x) * np.cos(n*2*np.pi/period * x)
a_n = lambda n : 2/period * quad(a_n_func, np.min(definition_interval), np.max(definition_interval), args=(n))[0]

b_n_func = lambda x, n : piecewise_func(x) * np.sin(n*2*np.pi/period * x)
b_n = lambda n : 2/period * quad(b_n_func, np.min(definition_interval), np.max(definition_interval), args=(n))[0]

sum_term = lambda x, n : a_n(n) * np.cos(n*2*np.pi/period * x) + b_n(n) * np.sin(n*2*np.pi/period * x)
def partial_sum(x, N):
    s = a_0/2
    for n in range(1, N+1):
        s += sum_term(x, n)
    return s

series_interval = np.linspace(0, 15, sample_size)
Ns = (5, 20, 50)
colors = [c for c in get_sub_cmap("viridis", .2, .8, N=len(Ns)).colors]

fig_sum, ax_sum = subplots()

ax_sum.plot(definition_interval, piecewise_func(definition_interval), ls="solid", color="tab:purple", label="Original")
for N, color in zip(Ns, colors):
    ax_sum.plot(series_interval, partial_sum(series_interval, N), ls="solid", color=color, label=f"N = {N}")

ax_sum.axvline(np.min(definition_interval), ls="dashed", color="tab:gray")
ax_sum.axvline(np.max(definition_interval), ls="dashed", color="tab:gray")

ax_sum.set_xlim(left=np.min(series_interval), right=np.max(series_interval))

ax_sum.set_xlabel(r"$x$")

ax_sum.legend(loc="best")

fig_sum.tight_layout()
fig_sum.savefig("numerical-methods/xabier/day-3/piecewise_fourier_sums.pdf", bbox_inches="tight")

fig_d, axs_d = subplots(1, 2, figsize=(12, 6))

ns = np.arange(1, 51)
a_ns = [a_n(n) for n in ns]
b_ns = [b_n(n) for n in ns]

axs_d[0].bar(ns, np.abs(a_ns), color="tab:purple")
axs_d[1].bar(ns, np.abs(b_ns), color="tab:orange")

axs_d[0].set_ylabel(r"$\left\vert a_n \right\vert$")
axs_d[1].set_ylabel(r"$\left\vert b_n \right\vert$")

for ax in axs_d:
    ax.set_xlabel(r"$n$")

    ax.set_xticks(ns[4::5])

fig_d.tight_layout()
fig_d.savefig("numerical-methods/xabier/day-3/piecewise_fourier_decay.pdf", bbox_inches="tight")
