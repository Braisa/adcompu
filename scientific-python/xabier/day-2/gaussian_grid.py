from random import gauss
from matplotlib.pyplot import subplot_mosaic
from cmasher import get_sub_cmap
from matplotlib.colors import AsinhNorm
from matplotlib.ticker import FixedFormatter

n = 1_000
points = [(gauss(), gauss()) for _ in range(n)]

origin_distances = [point[0]**2 + point[1]**2 for point in points]
sorted_origin_distances = sorted(origin_distances)
first_quadrant_distance_over_one = [point for i, point in enumerate(points) if origin_distances[i] > 1 and (point[0] > 0 and point[1] > 0)]

fig, axs = subplot_mosaic([["all", "sel", "dist"]], figsize=(15, 5), sharex=True, sharey=True)

fig.subplots_adjust(wspace=0)

axs["all"].scatter([point[0] for point in points], [point[1] for point in points], s=.5, color="tab:orange")

axs["all"].set_xlabel(r"$x$")
axs["all"].set_ylabel(r"$y$")

axs["all"].set_title("All points")

axs["sel"].scatter([point[0] for point in first_quadrant_distance_over_one], [point[1] for point in first_quadrant_distance_over_one], s=.5, color="tab:purple")

axs["sel"].set_xlabel(r"$x$")

axs["sel"].set_yticks([])

axs["sel"].set_title("First quadrant, distance over 1")

cmap = get_sub_cmap("viridis", .2, .8)
norm = AsinhNorm(vmin=sorted_origin_distances[0], vmax=sorted_origin_distances[-1])

cax = axs["dist"].scatter([point[0] for point in points], [point[1] for point in points], s=.5, c=cmap(norm(origin_distances)))

axs["dist"].set_xlabel(r"$x$")

axs["dist"].set_yticks([])

axs["dist"].set_title("Sorted by distance")

fig.colorbar(cax, location="right", orientation="vertical", fraction=.1, ticks=[0, 1], format=FixedFormatter([f"${norm.vmin:.4f}$", f"${norm.vmax:.4f}$"]))

fig.savefig("scientific-python/xabier/day-2/gaussian_grid.pdf", bbox_inches="tight")
