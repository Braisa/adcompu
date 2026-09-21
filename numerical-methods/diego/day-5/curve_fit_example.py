import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

DATA_FILE = "numerical-methods/diego/day-5/datafracs.txt"

data = np.loadtxt(DATA_FILE, unpack=True)

try:
    x, y, sy = data
except ValueError:
    x, y = data
    sy = np.zeros_like(y)

func = lambda x, A, B, C : A / ((x - B)**2 + (C/2)**2)

guess = (5e4, 75, 5e1)

popt, pcov = curve_fit(func, x, y, p0=guess, sigma=sy, absolute_sigma=True)

fig, ax = plt.subplots()

xlin = np.linspace(0, 200, 1000)

ax.errorbar(*data, capsize=4, color="tab:purple", fmt="o", ls=None)
ax.plot(xlin, func(xlin, *popt), ls="solid", color="tab:orange")

ax.set_xlim(left=np.min(xlin), right=np.max(xlin))

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y = \dfrac{A}{(x-B)^2 + (C/2)^2}$")

fig.savefig(f"numerical-methods/diego/day-5/curve_fit_example_{DATA_FILE.split("/")[-1].split(".")[0]}.pdf", bbox_inches="tight")
