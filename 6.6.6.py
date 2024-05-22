import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 6*x**3 + 3*x**2 + 8*x - 4

def find_extrema(f, a, b):
    df = lambda x: 4*x**3 - 18*x**2 + 6*x + 8

    critical_points = []
    for x in np.linspace(a, b, 100):
        if df(x) == 0:
            critical_points.append(x)

    critical_points.append(a)
    critical_points.append(b)

    extrema = [f(x) for x in critical_points]
    max_value = max(extrema)
    min_value = min(extrema)

    return max_value, min_value

max_value, min_value = find_extrema(f, -5, 5)
x = np.linspace(-5, 5, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x) = x^4 - 6x^3 + 3x^2 + 8x - 4')
plt.show()

print("наибольшее значение:", max_value)
print("наименьшее значение:", min_value)
