import numpy as np

def regression(x, y):
    x1 = np.transpose(x)
    x2 = np.dot(x1, x)
    if np.linalg.det(x2) != 0:
        x3 = np.linalg.inv(x2)
        b = np.dot(x3, np.dot(x1, y))
        return b
    else:
        print("det = 0")
        return None

def line_regression(x, y):
    n = np.shape(x)[0]
    e = np.array([np.array([1] * n)])
    concat = np.concatenate((e.T, x), axis = 1)
    return regression(concat, y)

def polynomial_regression(x, y, m):
    n = np.shape(x)[0]
    e = np.array([np.array([1] * n)])
    concat = np.concatenate((e.T, x), axis = 1)
    for i in range(2, m + 1):
        concat = np.concatenate((concat, x**i), axis = 1)
    return regression(concat, y)

def not_line_regression(x, y, func):
    n = np.shape(x)[0]
    m = len(func)
    e = np.array([np.array([1] * n)])
    concat = np.concatenate((e.T, x), axis = 1)
    for i in range(1, m + 1):
        concat = np.concatenate((concat, func[i - 1](x)), axis = 1)
    return regression(concat, y)

# def f1(x):
#     return x**2
# def f2(x):
#     return x
# def f3(x):
#     return x - 1
# def f4(x):
#     return x + 1

def k_fold(data, k):
    trainData = []
    testData = []
    train_test_data = []
    n = data.shape[0]
    m = n // k
    for i in range(1, k - 1):
        for j in range(n):
            if j < i * m and j >= (i - 1) * m:
                testData.append(data[j])
            else:
                trainData.append(data[j])
        train_test_data.append([trainData, testData])
        trainData.clear()
        testData.clear()
    return train_test_data

def cross_validation(train_test_data, regression_type, k):
    errors = []
    for i in range(k):
        train = train_test_data[i][0]
        test = train_test_data[i][1]
        x_tr = train[0], x_tst = test[0]
        y_tr = train[1], y_tst = test[1]
        beta = regression_type(x_tr, y_tr)
        err = 0
        for j in range(len(y_tst)):
            err += (y_tst[j] - beta * x_tst) ** 2
        err = err / len(y_tst)
        errors.append(err)
    return sum(errors) / k

#a = np.array([[2], [1], [1], [8]])
#b = np.array([[5], [0], [1], [0]])
#f = np.array([f1, f2, f3, f4])

#print(np.concatenate((a, b), axis=0))
#print(np.concatenate((a, b.T), axis=1))
#print(np.concatenate((b.T, a), axis=1))

#print(line_regression(a, b))
#print(polynomial_regression(a, b, 7))
#print(not_line_regression(a, b, f))
