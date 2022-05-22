# CRIAR UM PROGRAMA QUE AJUDA A RESOLVER LIMITES
import sympy as sp
sp.init_printing()

x, y = sp.symbols('x y', positive=True)

eq = (sp.tan(7*x))/sp.sin(3*x)
limite = sp.limit(eq, x, 0)

print(limite)
