import numpy as np
from numpy.fft import fft
from matplotlib.pyplot import subplot_mosaic

signal = np.loadtxt("numerical-methods/xabier/extras/piano.txt")

sampling_speed = 44_100
sample_number = len(signal)
sampling_start, sampling_end = 0, sample_number/sampling_speed
sampling_interval = np.linspace(sampling_start, sampling_end, sample_number, endpoint=False)
frequencies = np.arange(len(sampling_interval)) / (sampling_end - sampling_start)

coefficients = fft(signal)

fig, axs = subplot_mosaic([["signal", "signal"], ["power left", "power right"]], figsize=(12,8))

axs["signal"].plot(sampling_interval, signal, ls="solid")

axs["signal"].set_xlim(left=np.min(sampling_interval), right=np.max(sampling_interval))

axs["signal"].set_xlabel(r"$t$")
axs["signal"].set_ylabel(r"$f(t)$")

power_spectrum = np.abs(coefficients/len(sampling_interval))**2
for ax in (axs["power left"], axs["power right"]):
    ax.stem(frequencies, power_spectrum, basefmt=" ")

    ax.set_xlabel(r"$f_k$")


axs["power left"].set_ylabel(r"$\left\vert F_k \right\vert^2$")

fig.subplots_adjust(wspace=.04)

axs["power left"].set_xlim(left=0, right=1_500)
axs["power right"].set_xlim(left=44_100-1_500, right=44_100)

axs["power left"].spines.right.set_visible(False)
axs["power right"].spines.left.set_visible(False)

axs["power left"].yaxis.tick_left()
axs["power right"].yaxis.tick_right()
axs["power right"].tick_params(labelright=False)

d = .5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color="k", mec="k", mew=1, clip_on=False)

axs["power left"].plot([1, 1], [0, 1], transform=axs["power left"].transAxes, **kwargs)
axs["power right"].plot([0, 0], [0, 1], transform=axs["power right"].transAxes, **kwargs)

fig.savefig("numerical-methods/xabier/extras/piano.pdf", bbox_inches="tight")

print(f"Power peaks at frequency f = {np.argmax(power_spectrum)} Hz.")
print(f"Entering it at https://www.phys.unsw.edu.au/music/note/, it corresponds to a D6 plus 22 cents.")