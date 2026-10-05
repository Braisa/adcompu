import fractions
from numpy import isclose

f_13, f_64 = fractions.Fraction(1, 3), fractions.Fraction(6, 4)

print(dir(fractions.Fraction))

fh_10 = sum(fractions.Fraction(1, k) for k in range(1, 11))
h_10 = sum(1/k for k in range(1, 11))

print(f"\nExact result with fractions: H_10 = {fh_10}")
print(f"Result with floats: H_10 = {h_10}")
print(f"numpy.isclose -> {isclose(fh_10, h_10)}")

print(f"\nFraction(0.1) = {fractions.Fraction(.1)}")
print(f"Fraction({repr("0.1")}) = {fractions.Fraction(".1")}")
print("They differ because for the float a specific exact conversion is used; this is shown in help(Fraction).")
