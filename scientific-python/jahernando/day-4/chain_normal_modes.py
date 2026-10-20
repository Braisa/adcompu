import numpy as np
import scipy as sp
from matplotlib.pyplot import subplots, MultipleLocator

N = 10
k, m = 1., 1.

K = k * (2 * np.eye(N) - np.eye(N, k=1) - np.eye(N, k=-1))
print(f"K symmetric: {sp.linalg.issymmetric(K)}")

w, v = sp.linalg.eigh(K/m)

freqs = np.sqrt(w)
analytical = [2 * np.sqrt(k/m) * np.sin(j*np.pi/(2*N + 1)) for j in range(1, N+1)]
print(f"Average absolute deviation from analytical result: {np.mean(np.abs(freqs - analytical))}")

fig, axs = subplots(1, 3, figsize=(16, 4))

colors = ("tab:orange", "tab:purple", "tab:blue")

for m, (ax, col) in enumerate(zip(axs, colors)):
    ax.plot(np.arange(1, N+1), v[:, m], "o", color=col)

    ax.set_xlabel("Node")
    ax.set_ylabel("Deviation")

    ax.xaxis.set_major_locator(MultipleLocator(1))

    ax.set_title(f"Mode {m}")

fig.savefig("scientific-python/jahernando/day-4/chain_normal_modes.pdf", bbox_inches="tight")
