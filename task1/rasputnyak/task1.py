import numpy as np
import random


def f1(x):
    a = x[0]
    return a ** 3 - 4 * a ** 2 + 2 * a

def f2(x):
    a = x[0]
    b = x[1]
    return (1 - a ** 2) + 100 * ((b - a ** 2)) ** 2

def g1(x):
    a = x[0]
    return np.array([3 * a ** 2 - 8 * a + 2])

def g2(x):
    a = x[0]
    b = x[1]
    return np.array([-2 * a * (1 + 200 * (b - a ** 2)), 200 * (b - a ** 2)])

def g3(x):
    n = x.size
    a = np.array([0] * n)
    a[0] = -2 * (1 + 200 * (x[1] - (x[0])**2))
    for i in range(1, n - 1):
        a[i] = 200 * (x[i] - (x[i - 1])**2 - 2 * x[i] - 2 * x[i] * 200 * (x[i + 1] - (x[i])**2))
    a[n - 1] = 200 * (x[n - 1] - (x[n - 2])**2)
    return a


def gradient1(f, g, x0, l, e, u, v):
    x_j = x0 - l * g(x0)
    if abs(f(x_j) - f(x0)) > e and help(x_j, u, v) == True:
        return gradient1(f, g, x_j, l, e, u, v)
    else:
        return f(x_j), x_j

def gradient2(f, g, x0, l, e, u, v):
    x_j = x0 - l * g(x0)
    if abs(f(x_j) - f(x0)) > e and help(x_j, u, v) == True:
        l *= 0.9
        return gradient2(f, g, x_j, l, e, u, v)
    else:
        return f(x_j), x_j

def gradient3(f, g, x0, l, e, u, v):
    x_j = x0 - l * g(x0)
    if abs(f(x_j) - f(x0)) > e and help(x_j, u, v) == True:
        l = (dichotomy(f, np.array([0]), np.array([4]), g, np.array([2])))
        return gradient3(f, g, x_j, l, e, u, v)
    else:
        return f(x_j), x_j

def gradient_m_c(f, g, x0, l, e, n, u, v):
    x_j = monte_carlo(f, g, x0, l, n, u, v)
    if abs(f(x_j) - f(x0)) > e and help(x_j, u, v) == True:
        #l = (dichotomy(f, np.array([0]), np.array([4]), g, np.array([2])))
        return gradient_m_c(f, g, x_j, l, e, n, u, v)
    else:
        return f(x_j), x_j

def dichotomy(f, i, j, g, x0):
    a = i[0]
    b = j[0]
    if abs(a - b) > 0.5:
        d = random.uniform(0, ((b - a) / 2))
        l1 = np.array([(a + b) / 2 - d])
        l2 = np.array([(a + b) / 2 + d])
        f1 = f(x0 - l1 * g(x0))
        f2 = f(x0 - l2 * g(x0))
        if f1 > f2:
            return dichotomy(f, l1, j, g, x0)
        else:
            return dichotomy(f, i, l2, g, x0)
    else:
        return (a + b) / 2

def help(x, u, v):
    n = x.size
    k = 0
    for i in range(0, n):
        if x[i] >= u and x[i] <= v:
            k += 1
    if k == n:
        return True
    else:
        return False

def monte_carlo(f, g, x0, l, n, u, v):
    x_min = np.array([0] * n)
    for i in range(0, n):
        x_min[i] = random.uniform(u, v)
    f_min = f(x_min)
    for i in range(0, n):
        x = x_min - l * g(x_min)
        f_x = f(x)
        if f_x < f_min:
            x_min = x
    return x_min


#print(gradient_m_c(f1, g1, np.array([2]), 0.1, 0.1, 1, 0, 4))
#print(help(np.array([3, 2, 5]), 6))

#print(gradient2(f1, g1, np.array([2]), 0.1, 0.1, -20, -10))???
#print(gradient2(f2, g2, np.array([0.01, 0.01]), 0.1, 0.1, -0.1, 0.1))
#print(dichotomy(f1, np.array([0]), np.array([4]), g1, np.array([2])))

#print(g3(np.array([1, 0, 0, 0, 0, 1])))

