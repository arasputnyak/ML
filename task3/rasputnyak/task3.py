import numpy as np
import random
import math


def distance1(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def distance2(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def distance3(x, y):
    return max(abs(x[0] - y[0]), abs(x[1] - y[1]))

def splitData(data, k):
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

def kNN(test_train_data, k, distance):
    lst = []
    array = np.ndarray
    for i in range(len(test_train_data)):
        trainData = test_train_data[i, 0]
        testData = test_train_data[i, 1]
        for point in testData:
            for point1 in trainData:
                lst.append(distance(point, point1))
            np.concatenate((array, lst))
            ###


