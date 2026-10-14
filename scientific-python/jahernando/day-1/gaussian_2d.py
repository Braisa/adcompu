import numpy as np
from matplotlib.pyplot import subplots

u = lambda x, x0, sx : (x-x0)/sx
gaussian2d = lambda x, y, x0, y0, sx, sy, rho : np.exp(-(u(x, x0, sx)**2 + u(y, y0, sy)**2 - 2*rho*u(x, x0, sx)*u(y, y0, sy))/(2*(1-rho**2)))

rows, cols = 151, 101
xl, xr = -3, 3
yl, yr = -2, 2

x0, y0 = .6, -.2
sx, sy = .8, .5

xs = np.linspace(xl, xr, cols)
ys = np.linspace(yl, yr, rows)

X, Y = np.meshgrid(xs, ys)

rhos = (0, .6)
fig, axs = subplots(1, 2, figsize=(14, 6))

for ax, rho in zip(axs, rhos):
    Z = gaussian2d(X, Y, x0, y0, sx, sy, rho)

    rm, cm = np.unravel_index(np.argmax(Z), Z.shape)
    print(f"For rho = {rho}, maximum is {np.max(Z)} at x = {(cm * (xr-xl)/cols) + xl}, y = {(rm * (yr-yl)/rows) + yl}")

    ax.contourf(X, Y, Z, levels=20)

    ax.set_xlim(left=xl, right=xr)
    ax.set_ylim(bottom=yl, top=yr)

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")

    ax.set_title(f"$\{"rho"} = {rho}$")

fig.savefig("scientific-python/jahernando/day-1/gaussian_2d.pdf", bbox_inches="tight")
