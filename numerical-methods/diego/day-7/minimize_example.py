import numpy as np
from scipy.optimize import minimize

func_a = lambda x, y : x**2 + y**4 + x + y
func_b = lambda x, y : x**2 + y**2 + 8
func_c = lambda x, y : x * np.exp(-x**2 - y**2)

funcs = (func_a, func_b, func_c)

func_strings = (
    r"$x^2 + y^4 + x +y$",
    r"$x^2 + y^2 + 8$",
    r"$x\exp^{-(x^2 + y^2)}$"
)

bounds = (
    [(-5, 5), (-5, 5)],
    [(-10, 10), (-10, 10)],
    [(-1, 1), (-1, 1)]
)

guesses = (
    (0, 0),
    (0, 0),
    (0, 0)
)

func_wrapper = lambda z, func : func(*z)

for (func, func_string, bound, guess) in zip(funcs, func_strings, bounds, guesses):

    minimization = minimize(func_wrapper, guess, args=func, bounds=bound)

    print(f"Función: {func_string}")
    if not minimization.success:
        print(f"A minimización non foi exitosa:\n{minimization.message}")
    else:
        print(f"A minimización foi exitosa:\nx_0 = {minimization.x[0]:.6f}, y_0 = {minimization.x[1]:.6f}\n")