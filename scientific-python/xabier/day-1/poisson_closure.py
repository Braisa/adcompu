import numpy as np
from scipy.special import factorial
from functools import partial

poisson = lambda n, mu : mu**n * np.exp(-mu) / factorial(n)

def poisson_closure(mu):
    return partial(poisson, mu=mu)

poisson_5 = poisson_closure(5)
print(f"This should be about 1 ~= {sum([poisson_5(k) for k in range(0, 51)])}")
