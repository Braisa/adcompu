import numpy as np

operation_string = lambda title, operation, operand_a, operand_b, result : \
    f"{title}\n{operand_a}\n{operation}\n{operand_b}\n=\n{result}\n{"-"*25}"

analysis_string = lambda title, preamble, operand, result : \
    f"{title}\n{preamble}\n{operand}\né\n{result}\n{"."*25}"

poly_cubic = np.poly1d((1,-5,10,-12))
poly_square = np.poly1d((1,-5,4))

print(operation_string("SUMA", "+", poly_cubic, poly_square, np.polyadd(poly_cubic, poly_square)))

poly_cubic_two = np.poly1d((1,-4,5,-8))

print(operation_string("RESTA", "-", poly_cubic, poly_cubic_two, np.polysub(poly_cubic, poly_cubic_two)))

print(operation_string("PRODUCTO", "*", poly_cubic, poly_square, np.polymul(poly_cubic, poly_square)))

poly_quad = np.poly1d((1,-1,3,-1,1))
poly_square_two = np.poly1d((1,-1,1))

cociente, resto = np.polydiv(poly_quad, poly_square_two)

print(operation_string("COCIENTE", "/", poly_quad, poly_square_two, f"Cociente\n{cociente}\nResto\n{resto}"))

poly_square_three = np.poly1d((3,-3,-2))

print(analysis_string("DERIVADA", "A derivada en x=-1 de", poly_square_three, np.polyder(poly_square_three)(-1)))

print(analysis_string("INTEGRAL", "A integral con cte=5 de", poly_square_three, np.polyint(poly_square_three, k=5)))

poly_quin = np.poly1d((1,-11,49,-121,178,-120))

real_roots, complex_roots = [], []
for root in poly_quin.roots:
    if np.imag(root) != 0:
        complex_roots.append(root)
    else:
        real_roots.append(root)

print(f"As raíces do polinomio\n{poly_quin}\nson, reais\n{real_roots}\ne complexas\n{complex_roots}\n{"-"*25}")

poly_roots = np.array((2, np.complex128(1,2), np.complex128(1,-2), 3, 4))
poly_from_roots = np.poly1d(poly_roots, r=True)

print(f"O polinomio con raíces\n{poly_roots}\né\n{poly_from_roots}\n{"-"*25}")
