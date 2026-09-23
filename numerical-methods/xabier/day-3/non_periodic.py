import numpy as np
from matplotlib.pyplot import subplots
from scipy.integrate import quad

sample_size = 2000
period = 2
k = 8

non_periodic = lambda t : t**2

tlin = np.linspace(1, 3, sample_size)

a_0 = 2/period * quad(non_periodic, np.min(tlin), np.max(tlin))[0]

a_n_func = lambda x, n : non_periodic(x) * np.cos(n*2*np.pi/period * x)
a_n = lambda n : 2/period * quad(a_n_func, np.min(tlin), np.max(tlin), args=(n))[0]

b_n_func = lambda x, n : non_periodic(x) * np.sin(n*2*np.pi/period * x)
b_n = lambda n : 2/period * quad(b_n_func, np.min(tlin), np.max(tlin), args=(n))[0]

sum_term = lambda x, n : a_n(n) * np.cos(n*2*np.pi/period * x) + b_n(n) * np.sin(n*2*np.pi/period * x)
def partial_sum(x, N):
    s = a_0/2
    for n in range(1, N+1):
        s += sum_term(x, n)
    return s

fig, ax = subplots()

ax.plot(tlin, non_periodic(tlin), ls="solid", color="tab:purple", label="Original")
ax.plot(tlin, partial_sum(tlin, k), ls="solid", color="tab:orange", label=f"k = {k}")

ax.set_xlim(left=np.min(tlin), right=np.max(tlin))

ax.set_xlabel(r"$t$")

ax.legend(loc="best")

fig.tight_layout()
fig.savefig("numerical-methods/xabier/day-3/non_periodic.pdf", bbox_inches="tight")
