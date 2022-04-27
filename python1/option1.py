import sympy

for i in range(30, 61):
    factors = sympy.factorint(i)
    print(i, "prime" if len(factors) == 1 and factors.get(i) == 1 else "")
