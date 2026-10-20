import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
from matplotlib.pyplot import subplots

rng = np.random.default_rng(2664)
t = np.concatenate([rng.exponential(2.2, 2000),      # muon decays, tau = 2.2 us
                    rng.uniform(0, 10, 400)])        # flat background
t = t[t < 10]                                         # measured times (us)

counts, edges = np.histogram(t, bins=40, range=(0, 10))
centers = .5 * (edges[1:] + edges[:-1])

fig, ax = subplots()

ax.errorbar(centers, counts, fmt="o", yerr=np.sqrt(counts), capsize=4, color="tab:orange")

ax.set_yscale("log")

ax.set_xlabel(r"Lifetime ($\mu$s)")
ax.set_ylabel("Counts")

fig.savefig("scientific-python/jahernando/day-4/lifetime_measurement.pdf", bbox_inches="tight")

fit_function = lambda t, A, B, tau : A * np.exp(-t/tau) + B

popt, pcov = curve_fit(fit_function, centers, counts, p0=(centers[0], centers[-1], 2.), sigma=np.sqrt(counts), absolute_sigma=True)
punc = np.sqrt(np.diag(pcov))

print(f"Expected muon lifetime: 2.197 mus")
print(f"Fitted muon lifetime: {popt[-1]:.2f} +- {punc[-1]:.2f} mus")

chisq = np.sum(((counts - fit_function(centers, *popt))/np.sqrt(counts))**2)
pval = sp.stats.chi2.sf(chisq, len(counts) - 3)

print(f"Chi2: {chisq:.3f}")
print(f"p-value: {pval:.3f}")
print(f"The fit is not too good, as the chi2 and p-value are a bit high.")
