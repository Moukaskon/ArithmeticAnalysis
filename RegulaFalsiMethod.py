def func(x):
    return x ** 3 - 3 * x + 5

def newPoint(a, b):
    return (a * func(b) - b * func(a)) / (func(b) - func(a))


NMAX = 100

tol = 1 * 10 ** -4
a = 2
b = 3
counter = 0
x = newPoint(a, b)

while abs(func(x)) > tol and counter < NMAX:
    if func(a) * func(x) < 0:
        b = x
    else:
        a = x
    x = newPoint(a, b)
    counter += 1

print(x, counter, func(x))