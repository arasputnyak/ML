import numpy as np
from keras.datasets import mnist
from math import exp, log

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

class AdaBoost:
    def __init__(self, k):
        self.x = None
        self.y = None
        self.weights = None
        self.mask = None
        self.haar = None
        self.k = k
        self.alpha = None
        self.f = None

    def fit(self, x, y):
        self.x = X_train
        self.y = Y_train
        self.alpha = []
        self.weights = np.array([1 / len(y)] * len(y))
        self.mask = np.array([self.haar(784) for i in range(self.k)])
        for i in range(self.k):
            N = 0
            for j in range(len(self.y)):
                z = 0
                if np.dot(self.mask[i], self.x[j]) == y[j]:
                    z = 1
                N += self.weights[j] * z
            self.f[i] = np.argmin(N)
            self.alpha[i] = 0.5 * log((1 - N) / N)
            s = 0
            for j in range(self.k - 1):
                s += self.alpha[j] * self.f(x[j])
            self.weights[i] = exp(-y[i] * s)



