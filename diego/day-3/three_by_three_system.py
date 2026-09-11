import numpy as np
import scipy as sp

equation_string = lambda c1, c2, c3, b : f"{c1:.2f} x1 + {c2:.2f} x2 + {c3:.2f} x3 = {b:.2f}"

system_coefficients = np.array([[.3,.52,1],[.5,1,1.9],[.1,.3,.5]])
system_independents = np.array([-.01,.67,-.44])

system_solution = sp.linalg.inv(system_coefficients) @ system_independents

print(f"O sistema\n{equation_string(*system_coefficients[0], system_independents[0])}\n" \
      + f"{equation_string(*system_coefficients[1], system_independents[1])}\n" \
        + f"{equation_string(*system_coefficients[2], system_independents[2])}")
print(f"ten solución\nx1 = {system_solution[0]:.2f}\nx2 = {system_solution[1]:.2f}\nx3 = {system_solution[2]:.2f}")
