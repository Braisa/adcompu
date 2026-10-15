import numpy as np
from matplotlib.pyplot import subplot_mosaic
from scipy.interpolate import CubicSpline, make_smoothing_spline

rng = np.random.default_rng(2664)

xlin = np.linspace(0, 1, 200)
signal = np.sin(4*np.pi*xlin)

peak_center = int(.3*200)
signal[peak_center-2:peak_center+3] *= (-3, -4, -5, -4, -3)

signal[int(.7*200):] *= 4
signal += rng.normal(scale=.1, size=200)

remove = np.sort(rng.choice(200, size=80, replace=False))
xlin_cut, signal_cut = xlin[~remove][::-1], signal[~remove][::-1]

np_interp_reconstruction = np.interp(xlin, xlin_cut, signal_cut)
cubic_spline_reconstruction = CubicSpline(xlin_cut, signal_cut)
smoothing_spline_reconstruction = make_smoothing_spline(xlin_cut, signal_cut)

names = ("np interpolation", "Cubic spline", "Smoothing spline")
colors = ("tab:blue", "tab:green", "tab:purple")
reconstructions = (np_interp_reconstruction, cubic_spline_reconstruction(xlin), smoothing_spline_reconstruction(xlin))

fig, axs = subplot_mosaic([["sig", "err"]], figsize=(12, 6))

axs["sig"].plot(xlin_cut, signal_cut, ls="solid", color="tab:orange", label="Cut signal")

for name, col, reconstruction in zip(names, colors, reconstructions):
    axs["sig"].plot(xlin, reconstruction, ls="dashed", color=col, label=name)

    err = reconstruction - signal
    axs["err"].plot(xlin, err, ls="solid", color=col, label=name)

for axn in axs:
    axs[axn].set_xlim(left=np.min(xlin), right=np.max(xlin))
    
    axs[axn].legend(loc="best")

fig.savefig("scientific-python/jahernando/day-2/signal_reconstruction.pdf", bbox_inches="tight")
