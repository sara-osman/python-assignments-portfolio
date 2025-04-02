# Question 3
import numpy as np
def y (f,c,x):
    return f(c)+((f(c+10**-8)) - f(c-10**-8)) / (2*10**-8) * (x-c)

def x1x2 (f,c,e):
    n=0
    delta = 10**-6
    x1 = c
    x2 = c

    while abs(f(x1)- y(f, c, x1)) < e:
        x1 -= delta
        n += 1
        if n > 50000000:
            break

    while abs (f(x2)- y(f, c, x2)) < e:
        x2 -= delta
        n += 1
        if n > 50000000:
            break
        if n < 50000000:
            return x1, x2
        else:
            return "x1 and x2 cannot be found"

def f1(x):
    return x**2
def f2(x):
    return np.sin(x)
def f3(x):
    return np.exp(x)

print(x1x2(f1, 1, 0.1))
print(x1x2(f2, np.pi / 4, 0.05))
print(x1x2(f3, 0, 0.01))