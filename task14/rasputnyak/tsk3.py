import random, copy

def f(x):
    fc = 0
    n = x.shape[0]
    for i in range(n):
        fc += 2 * x[i]  + 1
    return fc

def gen_alg(repeat, f, dim, num, pr, bt):
    new_gen = generation(dim, num)
    for k in range(repeat):
        pairs = paIrs(new_gen, pr)
        new_chrome = two_point_cross(pairs, dim)
        mut = mutation(new_gen)
        mut2 = mutation(new_chrome)
        func = []
        all_ch = new_gen + new_chrome + mut + mut2
        for i in range(len(all_ch)):
            func.append(f(all_ch[i]))
        best = []
        bst = func[0]
        while len(best) < bt:
            for j in range(len(func)):
                if func[j] < bst:
                    bst = func[j]
                    l = j
            best.append(all_ch[l])
            func[l] = 66666
        new_gen = best
    massivchik = []
    for i in range(len(new_gen)):
        massivchik.append(f(new_gen[i]))
    answer = min(massivchik)
    return answer

def generation(dim, num):
    new_gen = []
    v = np.zeros(dim)
    for i in range(num):
        for j in range(dim):
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

def paIrs(new_gen, pr):
    num = len(new_gen)
    pairs = []
    for i in range(pr):
        r1 = random.randint(0, num - 1)
        r2 = random.randint(0, num - 1)
        pairs.append([new_gen[r1], new_gen[r2]])
    return pairs

def two_point_cross(pairs, dim):
    new_chrome = []
    r1 = random.randint(0, dim - 1)
    r2 = random.randint(0, dim - 1)
    if r1 > r2:
        r1, r2 = r2, r1
    for i in range(len(pairs)):
        a = pairs[i][0]
        b = pairs[i][1]
        chrome1 = np.zeros(dim)
        chrome2 = np.zeros(dim)
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

def mutation(chrome1):
    chrome = copy.deepcopy(chrome1)
    num = len(chrome)
    dim = len(chrome[0])
    for i in range(num):
        r = random.randint(1, dim - 2)
        chrome[i][r - 1], chrome[i][r + 1] = chrome[i][r + 1], chrome[i][r - 1]
    return chrome

print(gen_alg(30000, f, 5, 8, 3, 8))






