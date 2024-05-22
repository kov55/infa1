import sympy
t = sympy.Symbol("t")
x = sympy.Symbol("x")
b = -3 * (t - 1)
c = t + 4

uravn = sympy.solve(t * x**2 + b * x + c, x)
print("корни уравнения:", uravn)
