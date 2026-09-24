import numpy as np
from numpy.fft import fft
from matplotlib.pyplot import subplot_mosaic

f = 250

signal = lambda t : np.cos(2*np.pi*f*t)

sampling_start, sampling_end = 0, 5
sample_number = 10_000
sampling_interval = np.linspace(sampling_start, sampling_end, sample_number, endpoint=False)
frequencies = np.arange(len(sampling_interval)) / (sampling_end - sampling_start)

coefficients = fft(signal(sampling_interval))

fig, axs = subplot_mosaic([["signal", "signal", "signal"], ["real", "imag", "power"]], figsize=(12,8))

axs["signal"].plot(sampling_interval, signal(sampling_interval), ls="solid")

axs["signal"].set_xlim(left=np.min(sampling_interval), right=np.max(sampling_interval))

axs["signal"].set_xlabel(r"$t$")
axs["signal"].set_ylabel(r"$f(t)$")

axs["real"].stem(frequencies, np.real(coefficients), basefmt=" ")

axs["real"].set_ylabel(r"Re$(C_k)$")

axs["imag"].stem(frequencies, np.imag(coefficients), basefmt=" ")

axs["imag"].set_ylabel(r"Im$(C_k)$")

power_spectrum = np.abs(coefficients/len(sampling_interval))**2
axs["power"].stem(frequencies, power_spectrum, basefmt=" ")

axs["power"].set_ylabel(r"$\left\vert F_k \right\vert^2$")

for ax in (axs["real"], axs["imag"], axs["power"]):
    ax.set_xlabel(r"$f_k$")

fig.tight_layout()
fig.savefig("numerical-methods/xabier/day-4/fine_sampling.pdf", bbox_inches="tight")

rounded_spectrum = np.round(power_spectrum, 2)
peaks_freqs = np.nonzero(rounded_spectrum)
peaks_vals = power_spectrum[peaks_freqs]

print(f"Signal frequency: f = {f} Hz.")
print("After Fourier transform:")
for peak_freq, peak_val in zip(peaks_freqs[0], peaks_vals):
    print(f"Frequency peak at {frequencies[peak_freq]} Hz with power {peak_val:.3f}.")
