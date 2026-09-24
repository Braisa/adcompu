import numpy as np
from matplotlib.pyplot import subplots
from scipy.integrate import quad

funcs = (
    lambda t : 2*t + 4,
    lambda t : t**2,
    lambda t : .5 - np.heaviside(-t, 0)
)

periods = (3, 5, 2)

definition_bounds = ([-1, 2], [0, 5], [-1, 1])
extended_bounds = ([-1, 2], [-5, 10], [-3, 3])

names = ("Sawtooth", "Wavy", "Spiky")

interval_mapping = lambda x, original, target : ((x + np.min(target) - np.min(original)) % period) + np.min(target)

sample_size = 1000

fig, axs = subplots(1, 3, figsize=(18, 4))

for func, period, bounds, ex_bounds, ax, name in zip(funcs, periods, definition_bounds, extended_bounds, axs, names):

    definition_interval = np.linspace(bounds[0], bounds[1], sample_size)
    extended_interval = np.linspace(ex_bounds[0], ex_bounds[1], 3*sample_size)
    tlin = np.linspace(-period/2, period/2, sample_size)

    ax.plot(extended_interval, func(interval_mapping(extended_interval, extended_interval, definition_interval)), ls="solid", color="tab:purple", label="Original")

    ax.set_xlim(left=np.min(extended_interval), right=np.max(extended_interval))

    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$f(t)$")

    a_0 = 2/period * quad(func, np.min(tlin), np.max(tlin))[0]

    a_n_func = lambda x, n : func(interval_mapping(x, tlin, definition_interval)) * np.cos(n*2*np.pi/period * x)
    a_n = lambda n : 2/period * quad(a_n_func, np.min(tlin), np.max(tlin), args=(n))[0]

    b_n_func = lambda x, n : func(interval_mapping(x, tlin, definition_interval)) * np.sin(n*2*np.pi/period * x)
    b_n = lambda n : 2/period * quad(b_n_func, np.min(tlin), np.max(tlin), args=(n))[0]

    print(f"Function {name}")
    print(f"a_0 = {a_0}")
    print(f"a_1 = {a_n(1)}")
    print(f"a_2 = {a_n(2)}")
    print(f"b_1 = {b_n(1)}")
    print(f"b_2 = {b_n(2)}")

sum_term = lambda x, n : a_n(n) * np.cos(n*2*np.pi/period * x) + b_n(n) * np.sin(n*2*np.pi/period * x)
def partial_sum(x, N):
    s = a_0/2
    for n in range(1, N+1):
        s += sum_term(x, n)
    return s

axs[-1].plot(extended_interval, partial_sum(extended_interval, 2), ls="solid", color="tab:orange", label=r"$N = 2$")

axs[-1].legend(loc="upper right")

fig.savefig("numerical-methods/xabier/extras/various_functions.pdf", bbox_inches="tight")
