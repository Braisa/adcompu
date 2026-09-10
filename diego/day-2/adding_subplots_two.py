import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,9))

fig.suptitle("add_subplot")

fig.subplots_adjust(hspace=.6, wspace=.25)

ax_left = fig.add_subplot(3,2,1)

ax_left.set_xlabel(r"$x$")
ax_left.set_ylabel(r"$y$")

ax_left.set_xlim(left=0, right=3)
ax_left.set_ylim(bottom=0, top=.9)

ax_left.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax_left.yaxis.set_major_locator(plt.MultipleLocator(.2))

ax_left.set_title("add_subplot(3,2,1)")

ax_right = fig.add_subplot(3,2,2)

ax_right.set_xlabel(r"$x$")
ax_right.set_ylabel(r"$y$")

ax_right.set_xlim(left=0, right=3)
ax_right.set_ylim(bottom=0, top=.9)

ax_right.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax_right.yaxis.set_major_locator(plt.MultipleLocator(.2))

ax_right.set_title("add_subplot(3,2,2)")

ax_bottom = fig.add_subplot(3,2,(3,6))

ax_bottom.set_xlabel(r"$x$")
ax_bottom.set_ylabel(r"$y$")

ax_bottom.set_xlim(left=-2, right=2)
ax_bottom.set_ylim(bottom=-1, top=1)

ax_bottom.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax_bottom.yaxis.set_major_locator(plt.MultipleLocator(.25))

ax_bottom.set_title("add_subplot(3,2,(3,6))")

fig.savefig("diego/day-2/adding_subplots_two.pdf", bbox_inches="tight")
