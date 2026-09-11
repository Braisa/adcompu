import numpy as np
import scipy as sp

system_coefficients = np.array([[1,-2],[3,2]])
system_independents = np.array([1,11])

inverse_solution = np.dot(sp.linalg.inv(system_coefficients), system_independents)

solver_solution = sp.linalg.solve(system_coefficients, system_independents)

print(inverse_solution)
print(solver_solution)
