import sympy

for i in range(30, 61):
    print(i, "prime" if len(sympy.factorint(i)) == 1 else "")
