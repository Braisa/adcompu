import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "numerical-methods/diego/day-4/data0c.txt"

data = np.loadtxt(DATA_FILE, unpack=True)

fig, ax = plt.subplots()

ax.errorbar(*data, capsize=4, color="tab:orange", fmt="o", ls=None)

fig.savefig(f"numerical-methods/diego/day-4/checking_uncertainties_{DATA_FILE.split("/")[-1].split(".")[0]}.pdf", bbox_inches="tight")
