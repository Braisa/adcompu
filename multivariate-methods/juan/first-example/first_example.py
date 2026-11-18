import numpy as np
from matplotlib.pyplot import subplot_mosaic

mean = lambda z : sum(z) / len(z)
var = lambda z : sum((z - mean(z))**2) / len(z)
cov = lambda x, y : mean(x*y) - mean(x)*mean(y)
corr = lambda x, y : cov(x, y) / np.sqrt(var(x)) / np.sqrt(var(y))

data = np.genfromtxt("multivariate-methods/juan/first-example/datos_multivariate_clase_1.dat", usecols=(1,2))

x, y = data.T

fig, axs = subplot_mosaic([["yh", "sc"], ["ml", "xh"]], figsize=(10, 10))

axs["sc"].plot(x, y, ".", alpha=.2, color="tab:orange")

for axn in ("sc", "ml"):
    axs[axn].set_xlabel(r"$x$")
    axs[axn].set_ylabel(r"$y$")

for axn, d in zip(("xh", "yh"), (x, y)):
    axs[axn].hist(d, density=True, color="tab:purple")
    
    axs[axn].axvline(x=mean(d), ls="dashed", color="tab:orange")
    axs[axn].axvline(x=mean(d)-np.sqrt(var(d)), ls="dashed", color="tab:green")
    axs[axn].axvline(x=mean(d)+np.sqrt(var(d)), ls="dashed", color="tab:green")

    p5, median, p95 = np.percentile(d, 5), np.percentile(d, 50), np.percentile(d, 95)
    axs[axn].axvspan(xmin=p5, xmax=p95, alpha=.25, color="tab:gray")
    axs[axn].axvline(x=median, ls="dashed", color="tab:blue")

    axs[axn].set_xlabel(f"${axn[0]}$")

def sample_ml(x, y, sample_number=10, mode_sample_number=5, return_means=False):
    sample_size = (x.max() - x.min()) / sample_number
    sample_centers = x.min() + sample_size * (np.arange(0, sample_number) + .5)

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

    if return_means:
        return sample_centers, means
    else:
        return sample_centers, modes

for d, other_d, col, invert in zip((x, y), (y, x), ("tab:purple", "tab:blue"), (False, True)):
    sample_centers, modes = sample_ml(d, other_d, return_means=True)
    if not invert:
        axs["sc"].plot(sample_centers, modes, "o", color=col)
    else:
        axs["sc"].plot(modes, sample_centers, "o", color=col)

ml_value = lambda Q, z, q : mean(z) + corr(z, q) * np.sqrt(var(z)) / np.sqrt(var(q)) * (Q - mean(q))

ml_indices = np.random.choice(np.arange(0, len(data)), size=500, replace=True)
for axn in ("sc", "ml"):
    axs[axn].plot(x[ml_indices], ml_value(x[ml_indices], y, x), ls="solid", color="tab:purple")
    axs[axn].plot(ml_value(y[ml_indices], x, y), y[ml_indices], ls="solid", color="tab:blue")

ml_distributions = 500
distribution_sampling = 15
Y_ml = np.zeros((ml_distributions, distribution_sampling))
X_ml = Y_ml.copy()
for dist in range(ml_distributions):
    dist_data = data.copy()[np.random.choice(np.arange(0, len(data)), size=len(data), replace=True)]
    dist_x, dist_y = dist_data.T

    y_sample_centers, y_ml = sample_ml(dist_x, dist_y, sample_number=distribution_sampling, return_means=True)
    Y_ml[dist, :] = y_ml

    x_sample_centers, x_ml = sample_ml(dist_y, dist_x, sample_number=distribution_sampling, return_means=True)
    X_ml[dist, :] = x_ml

for sample_centers, D_ml, col, invert in zip((y_sample_centers, x_sample_centers), (Y_ml, X_ml), ("tab:purple", "tab:blue"), (False, True)):
    dist_p5s = [np.percentile(D_ml[:, j], 5) for j in range(distribution_sampling)]
    dist_p95s = [np.percentile(D_ml[:, j], 95) for j in range(distribution_sampling)]

    if not invert:
        axs["ml"].fill_between(sample_centers, dist_p5s, dist_p95s, alpha=.5, color=col)
    else:
        axs["ml"].fill_betweenx(sample_centers, dist_p5s, dist_p95s, alpha=.5, color=col)

fig.savefig("multivariate-methods/juan/first-example/first_example.pdf", bbox_inches="tight")

from matplotlib.pyplot import subplots
fig, axs = subplots(1, 5, figsize=(20, 4))
for a, ax in enumerate(axs):
    ax.hist(Y_ml[:, a], density=True)

fig.savefig("multivariate-methods/juan/first-example/hists.pdf", bbox_inches="tight")
