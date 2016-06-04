import numpy as np
import random, copy

def f(x):
    n = x.shape
    fc = np.array(n)
    for i in range(n):
        fc[i] = 3 * x[i] + 8
    return fc

def gen_alg(f, m, n, p, b):
    new_gen = generation(m, n)
    for k in range(k):
        pairs = paIrs(new_gen, p)
        new_chrome = two_point_cross(pairs, n)
        mut = mutation(new_gen, 0.01)
        mut2 = mutation(new_chrome, 0.01)
        func = []
        all_ch = new_gen + new_chrome + mut + mut2
        for i in range(len(all_ch)):
            func.append(f(all_ch[i]))
        best = []
        bst = func[0]
        while len(best) < b:
            for j in range(len(func)):
                if func[j] < bst:
                    bst = func[j]
                    l = j
            best.append(all_ch[l])
            func[l] = 66666
        new_gen = best

def generation(m, n):
    new_gen = []
    v = np.zeros(m)
    for i in range(n):
        for j in range(m):
            r = random.random()
            if r > 0.5:
                v[j] = 1
            else:
                v[j] = 0
        c = copy.deepcopy(v)
        new_gen.append(c)
    return new_gen

def fit(new_gen, f):
    func = []
    for i in range(len(new_gen)):
        func.append(f(new_gen[i]))
    return func

def paIrs(new_gen, p):
    n = len(new_gen)
    pairs = []
    for i in range(p):
        r1 = random.randint(0, n - 1)
        r2 = random.randint(0, n - 1)
        pairs.append([new_gen[r1], new_gen[r2]])
    return pairs

def two_point_cross(pairs, n):
    new_chrome = []
    r1 = random.randint(0, n - 1)
    r2 = random.randint(0, n - 1)
    if r1 > r2:
        r1, r2 = r2, r1
    for i in range(len(pairs)):
        a = pairs[i][0]
        b = pairs[i][1]
        chrome1 = np.zeros(n)
        chrome2 = np.zeros(n)
        for j in range(len(a)):
            if j < r1 or j > r2:
                chrome1[j] = a[j]
                chrome2[j] = b[j]
            else:
                chrome1[j] = b[j]
                chrome2[j] = a[j]
        c1 = copy.deepcopy(chrome1)
        c2 = copy.deepcopy(chrome2)
        new_chrome.append(c1)
        new_chrome.append(c2)
    return new_chrome

def mutation(chrome, v):
    r = random.randint(len(chrome))
    return chrome






