def func(x):
    return x ** 2 - 3

e = 0.00001
a = 1
b = 2
x = -1
result = -1
counter = 0
while b - a > e:
    x = (b + a)/2.0
    result = func(x)
    if result == 0:
        break
    elif func(b) * result < 0:
        a = x
    elif func(a) * result < 0:
        b = x
    counter += 1

print(x, counter)
