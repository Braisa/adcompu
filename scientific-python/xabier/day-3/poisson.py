from numpy import exp
from scipy.special import factorial
poisson = lambda n, mu : mu**n * exp(-mu) / factorial(n)