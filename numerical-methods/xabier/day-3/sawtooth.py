import numpy as np
from matplotlib.pyplot import subplots
from scipy.integrate import quad

sample_size = 2000
period = 4
k = 8

slope = lambda t : 1 - .5*t

definition_interval = np.linspace(0, 4, sample_size)
extension_interval = np.linspace(-4, 8, sample_size)

interval_mapping = lambda t, original, target : ((t + np.min(target) - np.min(original)) % period) + np.min(target)

a_0 = 2/period * quad(slope, np.min(definition_interval), np.max(definition_interval))[0]

a_n_func = lambda x, n : slope(x) * np.cos(n*2*np.pi/period * x)
a_n = lambda n : 2/period * quad(a_n_func, np.min(definition_interval), np.max(definition_interval), args=(n))[0]

b_n_func = lambda x, n : slope(x) * np.sin(n*2*np.pi/period * x)
b_n = lambda n : 2/period * quad(b_n_func, np.min(definition_interval), np.max(definition_interval), args=(n))[0]

sum_term = lambda x, n : a_n(n) * np.cos(n*2*np.pi/period * x) + b_n(n) * np.sin(n*2*np.pi/period * x)
def partial_sum(x, N):
    s = a_0/2
    for n in range(1, N+1):
        s += sum_term(x, n)
    return s

fig, ax = subplots()

ax.plot(extension_interval, slope(interval_mapping(extension_interval, extension_interval, definition_interval)), ls="solid", color="tab:purple", label="Original")
ax.plot(extension_interval, partial_sum(extension_interval, k), ls="solid", color="tab:orange", label=f"k = {k}")

ax.set_xlim(left=np.min(extension_interval), right=np.max(extension_interval))

ax.set_xlabel(r"$t$")

ax.legend(loc="best")

fig.tight_layout()
fig.savefig("numerical-methods/xabier/day-3/sawtooth.pdf", bbox_inches="tight")
