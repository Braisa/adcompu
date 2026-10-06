class Histogram:
    """
    Histogram custom class.
    """

    def __init__(self, nbins, xmin, xmax):
        if not isinstance(nbins, int):
            raise TypeError("nbins must be an integer")
        if not (isinstance(xmin, (int, float)) and isinstance(xmax, (int, float))):
            raise TypeError("xmin and xmax must both be numbers")
        if xmin >= xmax:
            raise ValueError("xmax must be greater than xmin")
        
        self.nbins = nbins
        self.xmin = xmin
        self.xmax = xmax

        self.bin_size = (self.xmax - self.xmin) / self.nbins

        self.counts = [0 for _ in range(nbins)]

    @property
    def entries(self):
        return sum(self.counts)

    def fill(self, x):
        if self.xmin <= x <= self.xmax:
            bin_index = int((x - self.xmin) // self.bin_size)
            self.counts[bin_index] += 1

    def mean(self):
        return sum([i*self.bin_size/2 * c for i, c in enumerate(self.counts)]) / self.nbins

    def __str__(self):
        return "".join([f"{c*"*"}\n" for c in self.counts])

if __name__ == "__main__":
    hist = Histogram(12, -3, 3)
    from random import gauss
    for _ in range(1000):
        hist.fill(gauss())
    print(hist)
