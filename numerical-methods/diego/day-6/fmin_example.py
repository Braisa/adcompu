import numpy as np
from scipy.optimize import fmin

parabole = lambda x : -1 + (x - 2)**2

left_bound, right_bound = -10, 10

minima = fmin(parabole, 0, full_output=True, disp=False)[0]

print(f"Os mínimos atopados para a función y = -1 + (x-2)^2 para -10 <= x <= 10 son:")
for minimum in minima:
    if left_bound <= minimum <= right_bound:
        print(f"x_min = {minimum:.4f}")
