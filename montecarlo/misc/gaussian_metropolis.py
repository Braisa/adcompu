import numpy as np
from matplotlib.pyplot import subplots
from tqdm import tqdm

gaussian = lambda x, mu, sigma : np.power(2*np.pi*sigma, -1/2) * np.exp(-(x-mu)**2/2/sigma**2)

mu, sigma = 0, 1
x_left, x_right = -5, 5

step_number = 10_000_000
step = .01
start = -1

x_steps = np.zeros(step_number)
x_steps[0] = start
for s in tqdm(range(1, step_number)):
    x_trial = x_steps[s-1] + step * (-1 + 2 * np.random.random())
    approval_rate = np.min((1., gaussian(x_trial, mu, sigma)/gaussian(x_steps[s-1], mu, sigma)))
    x_steps[s] = x_trial * int(approval_rate >= 1) + int(approval_rate < 1) * (x_trial + (x_steps[s-1] - x_trial) * int(approval_rate < np.random.random()))

x_steps = np.array(sorted(x_steps))

fig, ax = subplots()

xlin = np.linspace(x_left, x_right, 1000)
ax.plot(xlin, gaussian(xlin, mu, sigma), ls="solid", color="tab:orange")
ax.plot(x_steps, gaussian(x_steps, mu, sigma), ls="solid", color="tab:purple")

ax.set_xlim(left=np.min(xlin), right=np.max(xlin))

ax.set_xlabel(r"$x$")

fig.savefig("montecarlo/misc/gaussian_metropolis.pdf", bbox_inches="tight")
