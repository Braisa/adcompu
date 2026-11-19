import numpy as np
from matplotlib.pyplot import subplots, subplot_mosaic
from cmasher import get_sub_cmap
from tqdm import tqdm

data = np.genfromtxt("multivariate-methods/juan/kde/gwtc3all_confident.dat",
                     names=True, dtype=None, encoding=None)

kernel_1d = lambda x, x0, sigma : np.power(2*np.pi*sigma**2, -.5) * np.exp(-.5*(x - x0)**2/sigma**2)
kernel_2d = lambda x, y, x0, y0, sigma : kernel_1d(x, x0, sigma) * kernel_1d(y, y0, sigma)

m1 = data["mass_1_source"]
m1l, m1r = 0, 120
m1lin = np.arange(m1l, m1r, .1)

m2 = data["mass_2_source"]
m2l, m2r = 0, 80
m2lin = np.arange(0, 80, .1)

Fig, axs = subplot_mosaic([["m2", "sc"], ["ker", "m1"]], figsize=(10, 10))

for mi, ml, mr, mlin, axn in zip((m1, m2), (m1l, m2l), (m1r, m2r), (m1lin, m2lin), ("m1", "m2")):

    axs[axn].hist(mi, density=True, bins=10, alpha=.5)

    kernel_sigmas = (2, 5, 10)
    cs = get_sub_cmap("plasma", .2, .8, N=len(kernel_sigmas)).colors

    for kernel_sigma, c in zip(kernel_sigmas, cs):
        cumulative_kernel = np.zeros_like(mlin)
        for m in mi:
            m_kernel = kernel_1d(mlin, m, kernel_sigma)
            cumulative_kernel += m_kernel
            #ax.plot(mlin, m_kernel, ls="solid", alpha=.2, color="tab:orange")

        cumulative_kernel /= len(mi)
        axs[axn].plot(mlin, cumulative_kernel, ls="solid", color=c, label=f"$\sigma$ = {kernel_sigma}")

    axs[axn].set_xlim(left=ml, right=mr)

    axs[axn].set_xlabel(f"$m_{axn[-1]}$")

    axs[axn].legend(loc="best")

axs["sc"].plot(m1, m2, "o")
for axn in ("sc", "ker"):
    axs[axn].set_xlabel(r"$m_1$")
    axs[axn].set_ylabel(r"$m_2$")

sigma_2d = 5
M1, M2 = np.meshgrid(m1, m2)
M1l, M2l = np.meshgrid(m1lin, m2lin)
cumulative_kernel_2d = np.zeros_like(M1l)
for n1 in m1:
    for n2 in m2:
        mm_kernel_2d = kernel_2d(M1l, M2l, n1, n2, sigma_2d)
        cumulative_kernel_2d += mm_kernel_2d
cumulative_kernel_2d /= (len(m1) * len(m2))

cmap = get_sub_cmap("plasma", .2, .8)
axs["ker"].imshow(cumulative_kernel_2d, cmap=cmap, origin="lower")

Fig.savefig("multivariate-methods/juan/kde/m1m2.pdf", bbox_inches="tight")

fig, ax = subplots(subplot_kw={"projection" : "3d"})

ax.plot_wireframe(M1l, M2l, kernel_2d(M1l, M2l, m1[0], m2[0], 5), rstride=30, cstride=30)

fig.savefig("multivariate-methods/juan/kde/kernel_2d.pdf", bbox_inches="tight")
