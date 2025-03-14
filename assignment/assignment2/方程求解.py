def f(x):
    return x**3 - 5*(x**2) + 10*x - 80


def f1(x):
    return 3*(x**2) + 5*x + 10


x = 5
while abs(f(x)) > 0.00000001:
    x = x - f(x)/f1(x)
print(f'{x:.9f}')
