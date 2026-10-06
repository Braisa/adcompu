class Vector:

    """
    Vector custom class. Components are stored as a list.
    """

    def __init__(self, components):
        if not all([isinstance(c, (float, int)) for c in components]):
            raise TypeError("all components must be numbers")
        self.components = [c for c in components]

    def __len__(self):
        return len(self.components)
    
    def __getitem__(self, key):
        return self.components[key]

    def __repr__(self):
        return f"Vector({str(self.components)})"

    @classmethod
    def from_single_value(cls, value, dimension):
        if not isinstance(value, (float, int)):
            raise TypeError("value must be a number")
        return cls([value for _ in range(dimension)])

    def __add__(self, other):
        if isinstance(other, (float, int)):
            other = Vector.from_single_value(other, len(self))
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector([s + o for s, o in zip(self.components, other.components)])

    def __sub__(self, other):
        return self.__add__(other * -1)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            other = Vector.from_single_value(other, len(self))
        return all([s == o for s, o in zip(self.components, other.components)])

    def __mul__(self, value):
        if not isinstance(value, (float, int)):
            return NotImplemented
        return Vector([c * value for c in self.components])

    def __rmul__(self, value):
        return self * value

    def dot(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return sum([s * o for s, o in zip(self.components, other.components)])

    def __abs__(vector):
        if not isinstance(vector, Vector):
            return NotImplemented
        return vector.dot(vector)**.5
