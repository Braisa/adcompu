import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "diego/day-4/dataskips.txt"

fit_order = 3
actual_parameter_number = 2

data = np.loadtxt(DATA_FILE, unpack=True)

try:
    x, y, sy = data
except ValueError:
    x, y = data
    sy = np.ones_like(y)

N = len(x)

aux_a = np.zeros((fit_order+1, N))
for i in range(fit_order+1):
    aux_a[i,:] = x**i / sy

aux_b = (y / sy).T

coefficient_matrix = aux_a @ aux_a.T
independent_matrix = aux_a @ aux_b

# Necessary to trim matrix since fit skips some parameters

coefficient_matrix_trim = np.vstack((coefficient_matrix[0,::3], coefficient_matrix[-1,::3]))
independent_matrix_trim = np.vstack((independent_matrix[0], independent_matrix[-1]))

curve_matrix = np.linalg.inv(coefficient_matrix_trim)   
solution_matrix = curve_matrix @ independent_matrix_trim

print(solution_matrix)

fig, ax = plt.subplots()

lins = np.linspace(np.min(x), np.max(x), 1000)
fit = lambda x, a0, a3 : a0 + a3 * x**3

ax.errorbar(*data, capsize=4, color="tab:orange", fmt="o", ls=None)
ax.plot(lins, fit(lins, *solution_matrix), color="tab:purple", ls="solid")

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

fig.savefig(f"diego/day-4/fitting_skip_{DATA_FILE.split("/")[-1].split(".")[0]}.pdf", bbox_inches="tight")

chisq = np.sum((y - fit(x, *solution_matrix))**2 / sy**2)

std_dev = np.sqrt(N*chisq / ((N-actual_parameter_number-1) * np.sum(sy**-2)))

y_mean = np.sum(y**2 / sy**2) / np.sum(sy**-2)

y_mean_dev = np.sum((y - y_mean)**2 / sy**2)

rsq = (y_mean_dev - chisq) / y_mean_dev

solution_unc = np.sqrt(np.diag(curve_matrix))

if sy.all() == 1:
    solution_unc *= std_dev

result_string = lambda name, value : f"{name} = {value:.6f}"
parameter_string = lambda name, value, unc : f"{name} = {value:.5f} ({unc:.5f})"

print(result_string("chi squared", chisq))
print(result_string("Standard deviation", std_dev))
print(result_string("Mean y", y_mean))
print(result_string("Determination coefficient", rsq))

for i, (fit_parameter, fit_unc) in enumerate(zip(solution_matrix.ravel(), solution_unc)):
    print(parameter_string(f"Fit parameter of order {i}", fit_parameter, fit_unc))