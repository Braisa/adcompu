import numpy as np
from matplotlib.pyplot import subplot_mosaic

mean = lambda z : sum(z) / len(z)
var = lambda z : sum((z - mean(z))**2) / len(z)
cov = lambda x, y : mean(x*y) - mean(x)*mean(y)
corr = lambda x, y : cov(x, y) / np.sqrt(var(x)) / np.sqrt(var(y))

data = np.genfromtxt("multivariate-methods/juan/day-1/datos_multivariate_clase_1.dat", usecols=(1,2))

x, y = data.T

fig, axs = subplot_mosaic([["yh", "sc"], ["yml", "xh"]], figsize=(10, 10))

axs["sc"].plot(x, y, ".", alpha=.2, color="tab:orange")

axs["sc"].set_xlabel(r"$x$")
axs["sc"].set_ylabel(r"$y$")

for axn, d in zip(("xh", "yh"), (x, y)):
    axs[axn].hist(d, density=True, color="tab:purple")
    
    axs[axn].axvline(x=mean(d), ls="dashed", color="tab:orange")
    axs[axn].axvline(x=mean(d)-np.sqrt(var(d)), ls="dashed", color="tab:green")
    axs[axn].axvline(x=mean(d)+np.sqrt(var(d)), ls="dashed", color="tab:green")

    p5, median, p95 = np.percentile(d, 5), np.percentile(d, 50), np.percentile(d, 95)
    axs[axn].axvspan(xmin=p5, xmax=p95, alpha=.25, color="tab:gray")
    axs[axn].axvline(x=median, ls="dashed", color="tab:blue")

    axs[axn].set_xlabel(f"${axn[0]}$")

sample_number = 10
sample_size = (x.max() - x.min()) / sample_number
sample_centers = x.min() + sample_size * np.arange(0, sample_number)

y_xsel = []
for k in range(sample_number):
    mask = np.where((k*sample_size < x - x.min()) & ((k+1)*sample_size > x - x.min()))[0]
    y_xsel.append(y[mask])

mode_sample_number = 5
modes, means = [], []
for sample in y_xsel:
    mode_sample_size = (sample.max() - sample.min()) / mode_sample_number

    y_counter = np.zeros(mode_sample_number)
    for l in range(len(y_counter)):
        mask = np.where((l*mode_sample_size < sample - sample.min()) & ((l+1)*mode_sample_size > sample - sample.min()))[0]
        y_counter[l] = len(sample[mask])
    modes.append(sample.min() + mode_sample_size * np.argmax(y_counter))

    means.append(mean(sample))

axs["sc"].plot(sample_centers, modes, "o", color="tab:purple")
axs["sc"].plot(sample_centers, means, "o", color="tab:blue")

fig.savefig("multivariate-methods/juan/day-1/first_example.pdf", bbox_inches="tight")
