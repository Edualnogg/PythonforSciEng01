import sympy as sp

sp.init_printing()
x, y = sp.symbols('x y')

eq = x**2 + x*y + y**2

eq1 = sp.factor(2*x**2 + x*y + y**2)
print(eq1)
