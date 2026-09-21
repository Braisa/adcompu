import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

sigma, r, b = 10, 8/3, 28

system = lambda t, x, y, z : (sigma*(y - x), r*x - y - x*z, x*y - b*z)
system_wrapped = lambda t, z : system(t, *z)

times = np.linspace(0, 12, 1000)

initial_values = [5, 5, 5]

solution = solve_ivp(system_wrapped, (np.min(times), np.max(times)), initial_values, t_eval=times)

fig = plt.figure(figsize=(10, 10))

ax_zx = fig.add_subplot(2, 2, 1)

ax_zx.plot(solution.y[0], solution.y[2], ls="solid", color="tab:orange")

ax_zx.set_xlabel(r"$x$")
ax_zx.set_ylabel(r"$z$")

ax_zy = fig.add_subplot(2, 2, 3)

ax_zy.plot(solution.y[1], solution.y[2], ls="solid", color="tab:orange")

ax_zy.set_xlabel(r"$y$")
ax_zy.set_ylabel(r"$z$")

ax_yx = fig.add_subplot(2, 2, 2)

ax_yx.plot(solution.y[0], solution.y[1], ls="solid", color="tab:purple")

ax_yx.set_xlabel(r"$x$")
ax_yx.set_ylabel(r"$y$")

ax_zxy = fig.add_subplot(2, 2, 4, projection="3d")

X, Y = np.meshgrid(solution.y[0], solution.y[1])
_, Z = np.meshgrid(solution.y[0], solution.y[2])

ax_zxy.plot_wireframe(X, Y, Z, rstride=2, cstride=2, color="tab:blue")

ax_zxy.set_xlabel(r"$x$")
ax_zxy.set_ylabel(r"$y$")
ax_zxy.set_zlabel(r"$z$")

fig.savefig("numerical-methods/diego/day-8/lorenz_system.pdf", bbox_inches="tight")
