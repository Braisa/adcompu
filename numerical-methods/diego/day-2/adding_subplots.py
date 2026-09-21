import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))

fig.suptitle("add_subplot")

ax_left = fig.add_subplot(2, 2, (1,3))

ax_left.set_xlabel(r"$x$")
ax_left.set_ylabel(r"$y$")

ax_left.set_xlim(left=0, right=3)
ax_left.set_ylim(bottom=0, top=.9)

ax_left.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax_left.yaxis.set_major_locator(plt.MultipleLocator(.1))

ax_left.set_title("add_subplot(2,2,(1,3))")

ax_top = fig.add_subplot(2, 2, 2)

ax_top.set_xlabel(r"$x$")
ax_top.set_ylabel(r"$y$")

ax_top.set_xlim(left=0, right=6)
ax_top.set_ylim(bottom=0, top=2)

ax_top.xaxis.set_major_locator(plt.MultipleLocator(1))
ax_top.yaxis.set_major_locator(plt.MultipleLocator(.5))

ax_top.set_title("add_subplot(2,2,2)")

ax_bottom = fig.add_subplot(2, 2, 4)

ax_bottom.set_xlabel(r"$x$")
ax_bottom.set_ylabel(r"$y$")

ax_bottom.set_xlim(left=-2, right=2)
ax_bottom.set_ylim(bottom=-1, top=1)

ax_bottom.xaxis.set_major_locator(plt.MultipleLocator(1))
ax_bottom.yaxis.set_major_locator(plt.MultipleLocator(.5))

ax_bottom.set_title("add_subplot(2,2,4)")

fig.savefig("diego/day-2/adding_subplots.pdf", bbox_inches="tight")
