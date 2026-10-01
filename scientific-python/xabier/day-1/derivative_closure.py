import numpy as np
from matplotlib.pyplot import subplots
from functools import partial

def derivative(f, h=1e-5, method="central"):
    def approx(x):
        if method == "central":
            return (f(x+h) - f(x-h))/2/h
        elif method == "forward":
            return (f(x+h) - f(x))/h
    return approx

fig, ax = subplots()

xlin = np.linspace(-np.pi, np.pi, 1000)

ax.plot(xlin, np.sin(xlin), ls="solid", color="tab:blue", label=r"$\sin x$")
ax.plot(xlin, np.cos(xlin), ls="dashed", color="tab:purple", label=r"$\cos x$")
ax.plot(xlin, derivative(np.sin)(xlin), ls="dotted", color="tab:orange", label="approx")

ax.set_xlim(left=np.min(xlin), right=np.max(xlin))
ax.set_ylim(bottom=-1, top=1)

ax.set_xlabel(r"$x$")

ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.set_yticks([-1, -.5, 0, .5, 1])

ax.set_xticklabels([r"$-\pi$", r"$-\dfrac{\pi}{2}$", r"$0$", r"$\dfrac{\pi}{2}$", r"$\pi$"])

ax.legend(loc="best")

fig.savefig("scientific-python/xabier/day-1/derivative_closure.pdf", bbox_inches="tight")

relative_error = lambda f, x : np.abs((f(x) - np.cos(x))/np.cos(x))
relative_error_1 = partial(relative_error, x=1)

steps = .1 / 10**np.arange(8)
steps_ticks = np.arange(len(steps))

fig_e, ax_e = subplots()

ax_e.bar(steps_ticks, relative_error_1(derivative(np.sin, method="central")), align="edge", width=+.4, color="tab:purple", label="Central")
ax_e.bar(steps_ticks, relative_error_1(derivative(np.sin, method="forward")), align="edge", width=-.4, color="tab:orange", label="Forward")

ax_e.set_yscale("log")

ax_e.set_xlabel(r"$h$")
ax_e.set_ylabel(r"Relative error at $x=1$")

ax_e.set_xticks(steps_ticks)

ax_e.set_xticklabels([f"{step:.0E}" for step in steps])

ax_e.legend(loc="center")

fig_e.savefig("scientific-python/xabier/day-1/derivative_closure_error.pdf", bbox_inches="tight")
