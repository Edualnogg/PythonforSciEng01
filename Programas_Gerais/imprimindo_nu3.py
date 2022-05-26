'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14...

'''


def f(x: float) -> 30:
    pass


a = f.__annotations__['x']  # float
b = f.__annotations__['return']  # 30
print(a, '\n', b)
