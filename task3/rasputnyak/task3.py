import numpy as np
import random
import math
#import sklearn


def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def splitTrainTest (data, testPercent):
    trainData = []
    testData  = []
    for row in data:
        if random.random() < testPercent:
            testData.append(row)
        else:
            trainData.append(row)
    return trainData, testData


def kNN(trainData, testData, x, k):
    lst = []
    #lst2 = []
    #for testPoint in testData:
        #testDist = [ [distance(testPoint, trainData[i][0]), trainData[i][1]] for i in range(len(trainData))]

    for i in range(0, trainData.size):
        lst.append(distance(x, trainData[i]))
    lst.sort()
    lst2 = lst[0:k + 1]

    dist = []
    for point in testData:
        dist.append([distance(point, trainData[i])] for i in range(testData.size))


