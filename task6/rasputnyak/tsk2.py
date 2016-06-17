import numpy as np
#from keras.datasets import mnist
from math import exp, log
import random

#(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

class AdaBoost:
    def __init__(self, k):
        self.x = None
        self.y = None
        self.weights = None
        self.mask = None
        self.k = k
        self.alpha = None
        self.func = None

    def fit(self, x, y):
        #self.x = X_train
        #self.y = Y_train
        self.alpha = []
        self.weights = np.array([1 / len(y)] * len(y))
        self.mask = np.array([generation_haar() for i in range(self.k)])
        for i in range(self.k):
            N = 0
            for j in range(len(self.y)):
                z = 0
                if np.dot(self.mask[i], self.x[j]) == -y[j]:
                    z = 1
                N += self.weights[j] * z
            self.func[i] = np.argmin(N)
            self.alpha[i] = 0.5 * log((1 - N) / N)
            for j in range(self.k - 1):
                self.weights[i] *= exp(-self.alpha[i] * y[j] * self.func[i])
            w = sum(self.weights)
            for j in range(len(y)):
                self.weights[j] = self.weights[j] / w

def generation_haar():
    haar = np.ones((28, 28))
    r1 = random.randint(10, 15)
    r2 = random.randint(15, 20)
    r3 = random.randint(0, 28 - r1)
    r4 = random.randint(0, 28 - r2)
    for j in range(r3, r1 + r3):
        for h in range(r4, r2 + r4):
            haar[j][h] = -1

