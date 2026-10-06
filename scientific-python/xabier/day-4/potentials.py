from abc import ABC, abstractmethod

class Potential1D(ABC):
    """
    Abstract base class for one-dimensional potentials.
    """

    @abstractmethod
    def V(self, x):
        """
        Returns the potential at a given point x.
        """

    def force(self, x, h=1e-5):
        """
        Computes the force at a given point x using a central difference.
        """
        return -1 * ((self.V(x + h) - self.V(x - h)) / 2 / h)

    def describe(self):
        """
        Returns a string with the name.
        """
        return f"{type(self).__name__}"

class Harmonic(Potential1D):
    """
    Harmonic potential class. Derived from Potential1D.
    """

    def __init__(self, k):
        if not isinstance(k, (float, int)):
            raise TypeError("k must be a number")
        if not k > 0:
            raise ValueError("k must be a positive number")

        self.k = k

    def V(self, x):
        return .5 * self.k * x**2

class Gravity(Potential1D):
    """
    Gravity potential class. Derived from Potential1D.
    """

    def __init__(self, m , g=9.81):
        if not isinstance(g, (float, int)):
            raise TypeError("g must be a number")
        if not isinstance(m, (float, int)):
            raise TypeError("m must be a number")
        if not m > 0:
            raise ValueError("m must be a positive number")

        self.m = m
        self.g = g

    def V(self, x):
        return self.m * self.g * x

if __name__ == "__main__":

    harm = Harmonic(1)
    grav = Gravity(1)

    from numpy import linspace
    xlin = linspace(-1, 1, 1000)

    from matplotlib.pyplot import subplot_mosaic
    fig, axs = subplot_mosaic([["hv", "hf"], ["gv", "gf"]], figsize=((12, 12)))

    axs["hv"].plot(xlin, harm.V(xlin), ls="solid", color="tab:orange")
    axs["hv"].set_ylabel(r"$V(x)$")
    axs["hv"].set_title("Harmonic($k=1$)")

    axs["hf"].plot(xlin, harm.force(xlin), ls="solid", color="tab:orange", label="Approx")
    axs["hf"].plot(xlin, -harm.k * xlin, ls="dashed", color="tab:purple", label="Exact")
    axs["hf"].set_ylabel(r"$f(x)$")
    axs["hf"].set_title("Harmonic force comparison")
    axs["hf"].legend(loc="best")

    axs["gv"].plot(xlin, grav.V(xlin), ls="solid", color="tab:orange")
    axs["gv"].set_ylabel(r"$V(x)$")
    axs["gv"].set_title("Gravity($m=1$)")

    axs["gf"].plot(xlin, grav.force(xlin), ls="solid", color="tab:orange", label="Approx")
    axs["gf"].axhline(-grav.m * grav.g, ls="dashed", color="tab:purple", label="Exact")
    axs["gf"].set_ylabel(r"$f(x)$")
    axs["gf"].set_title("Gravity force comparison")
    axs["gf"].legend(loc="best")
    axs["gf"].set_ylim(bottom=-1.05*grav.g, top=-.95*grav.g) # or else it gets crazy

    for name in axs:
        axs[name].set_xlim(left=min(xlin), right=max(xlin))
        axs[name].set_xlabel(r"$x$")

    fig.savefig("scientific-python/xabier/day-4/potentials.pdf", bbox_inches="tight")
