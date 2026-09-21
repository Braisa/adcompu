import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15,12))

fig.suptitle("ejemplo subplots")

fig.subplots_adjust(hspace=.5, wspace=.4)

ax_top = fig.add_subplot(3,3,(1,3))

ax_top.set_xlabel(r"$x$")
ax_top.set_ylabel(r"$y$")

ax_top.set_xlim(left=0, right=3)
ax_top.set_ylim(bottom=0, top=.9)

ax_top.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax_top.yaxis.set_major_locator(plt.MultipleLocator(.2))

ax_top.set_title("subplot(3,3,(1,3))")

ax_center = fig.add_subplot(3,3,(4,5))

ax_center.set_xlabel(r"$x$")
ax_center.set_ylabel(r"$y$")

ax_center.set_xlim(left=0, right=3)
ax_center.set_ylim(bottom=0, top=.9)

ax_center.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax_center.yaxis.set_major_locator(plt.MultipleLocator(.2))

ax_center.set_title("subplot(3,3,(4,5))")

ax_right = fig.add_subplot(3,3,(6,9))

ax_right.set_xlabel(r"$x$")
ax_right.set_ylabel(r"$y$")

ax_right.set_xlim(left=-2, right=2)
ax_right.set_ylim(bottom=-1, top=1)

ax_right.xaxis.set_major_locator(plt.MultipleLocator(1))
ax_right.yaxis.set_major_locator(plt.MultipleLocator(.25))

ax_right.set_title("subplot(3,3,(6,9))")

ax_corner = fig.add_subplot(3,3,7)

ax_corner.set_xlabel(r"$x$")
ax_corner.set_ylabel(r"$y$")

ax_corner.set_xlim(left=0, right=3)
ax_corner.set_ylim(bottom=0, top=.9)

ax_corner.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax_corner.yaxis.set_major_locator(plt.MultipleLocator(.2))

ax_corner.set_title("subplot(3,3,7)")

ax_bottom = fig.add_subplot(3,3,8)

ax_bottom.set_xlabel(r"$x$")
ax_bottom.set_ylabel(r"$y$")

ax_bottom.set_xlim(left=0, right=3)
ax_bottom.set_ylim(bottom=0, top=.9)

ax_bottom.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax_bottom.yaxis.set_major_locator(plt.MultipleLocator(.2))

ax_bottom.set_title("subplot(3,3,8)")

fig.savefig("diego/day-2/adding_subplots_three.pdf", bbox_inches="tight")
