import numpy as np
from scipy.optimize import fmin
import matplotlib.pyplot as plt

sine = lambda x : -5 - np.sin(x)/x

left_bound, right_bound = -15, 15
step = 1e-1
rounding, tolerance = 3, 1e-8

minima = []
for guess in np.arange(left_bound, right_bound, step):
    minimum = np.round(fmin(sine, guess, xtol=tolerance, ftol=tolerance, disp=False)[0], rounding)
    if not minimum in minima:
        minima.append(minimum)

print(f"Os mínimos atopados para a función y = -5 - sen(x)/x para -15 <= x <= 15 son:")
for minimum in minima:
    if left_bound <= minimum <= right_bound:
        print(f"x_min = {minimum:.4f}")

print(f"O mínimo absoluto atopado para a función y = -5 - sen(x)/x para -15 <= x <= 15 é:")
abs_min = minima[np.argmax(sine(minima))]
if left_bound <= abs_min <= right_bound:
    print(f"x_min,abs = {abs_min:.4f}")

reciprocal_sine = lambda x : sine(x)**-1

maxima = []
for guess in np.arange(left_bound, right_bound, step):
    maximum = np.round(fmin(reciprocal_sine, guess, xtol=tolerance, ftol=tolerance, disp=False)[0], rounding)
    if not maximum in maxima:
        maxima.append(maximum)
# Remove zero manually, maybe it is detected as minima because of a quirk of the reciprocal?
maxima.pop(np.argmin(np.abs(maxima)))

print(f"Os máximos atopados para a función y = -5 - sen(x)/x para -15 <= x <= 15 son:")
for maximum in maxima:
    if left_bound <= maximum <= right_bound:
        print(f"x_max = {maximum:.4f}")

fig, axs = plt.subplots(2, 1, sharex=True)

xlin = np.linspace(left_bound, right_bound, 1000)

axs[1].plot(xlin, sine(xlin), ls="solid", color="tab:orange")
for minimum in minima:
    axs[1].axvline(minimum, ls="dashed", color="tab:blue")

axs[0].plot(xlin, reciprocal_sine(xlin), ls="solid", color="tab:purple")
for maximum in maxima:
    axs[1].axvline(maximum, ls="dashed", color="tab:red")
    axs[0].axvline(maximum, ls="dashed", color="tab:red")

axs[1].set_xlabel(r"$x$")

axs[1].set_ylabel(r"$-5 - sen(x)/x$")
axs[0].set_ylabel(r"$(-5 - sen(x)/x)^{-1}$")

axs[1].set_xlim(left=left_bound, right=right_bound)

fig.savefig("numerical-methods/diego/day-6/fmin_sine.pdf", bbox_inches="tight")
