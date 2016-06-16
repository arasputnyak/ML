import copy
import math
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target

def distance1(x, y):
    s = 0
    for i in range(4):
        s += (x[i] - y[i]) ** 2
    return math.sqrt(s)

def distance2(x, y):
    s = 0
    for i in range(4):
        s += abs(x[i] - y[i])
    return s

def splitData(data, k):
    trainData = []
    testData = []
    train_test_data = []
    n = data.shape[0]
    m = n // k
    for i in range(1, k + 1):
        for j in range(n):
            if j < i * m and j >= (i - 1) * m:
                testData.append(data[j])
            else:
                trainData.append(data[j])
        one = copy.deepcopy(trainData)
        two = copy.deepcopy(testData)
        train_test_data.append([one, two])
        trainData.clear()
        testData.clear()
    return train_test_data

def num_of_elem(lst, elem, k):
    count = 0
    for i in range(k):
        if lst[i] == elem:
            count +=1
    return count

def kNN(test_train_data_X, test_train_data_Y, k, distance):
    lst = []
    lst2 = []
    lst3 = []
    for i in range(len(test_train_data_X)):
        trainData = test_train_data_X[i][0]
        testData = test_train_data_X[i][1]
        trn_Y = test_train_data_Y[i][0]
        l1 = len(testData)
        l2 = len(trainData)
        for h in range(l1):
            lst.append([])
        for h in range(l1):
            lst2.append([])
        for h in range(l1):
            lst3.append([])
        for h in range(l2):
            for m in range(l1):
                lst[m].append(distance(trainData[h], testData[m]))
        for h in range(l1):
            lst2[h] = copy.deepcopy(trainData)
            lst3[h] = copy.deepcopy(trn_Y)
            for m in reversed(range(l2)):
                for l in range(1, m + 1):
                    if lst[h][l - 1] > lst[h][l]:
                        lst[h][l], lst[h][l - 1] = lst[h][l - 1], lst[h][l]
                        lst2[h][l], lst2[h][l - 1] = lst2[h][l - 1], lst2[h][l]
                        lst3[h][l], lst3[h][l - 1] = lst3[h][l - 1], lst3[h][l]
        answer = []
        for h in range(l1):
            class_one = num_of_elem(lst3[h], 0, k)
            class_two = num_of_elem(lst3[h], 1, k)
            class_three = num_of_elem(lst3[h], 2, k)
            maxx = max(class_one, class_two, class_three)
            ans = -1
            if maxx == class_one:
                ans = 0
            if maxx == class_two:
                ans = 1
            if maxx == class_three:
                ans = 2
            answer.append(ans)
        q = []
        for h in range(l1):
            q.append([])
        for h in range(l1):
            q[h] = testData[h], answer[h]
        print(q)

def weighted_kNN(test_train_data_X, test_train_data_Y, k, distance, a):
    lst = []
    lst2 = []
    lst3 = []
    for i in range(len(test_train_data_X)):
        trainData = test_train_data_X[i][0]
        testData = test_train_data_X[i][1]
        trn_Y = test_train_data_Y[i][0]
        l1 = len(testData)
        l2 = len(trainData)
        for h in range(l1):
            lst.append([])
        for h in range(l1):
            lst2.append([])
        for h in range(l1):
            lst3.append([])
        for h in range(l2):
            for m in range(l1):
                lst[m].append(distance(trainData[h], testData[m]))
        for h in range(l1):
            lst2[h] = copy.deepcopy(trainData)
            lst3[h] = copy.deepcopy(trn_Y)
            for m in reversed(range(l2)):
                for l in range(1, m + 1):
                    if lst[h][l - 1] > lst[h][l]:
                        lst[h][l], lst[h][l - 1] = lst[h][l - 1], lst[h][l]
                        lst2[h][l], lst2[h][l - 1] = lst2[h][l - 1], lst2[h][l]
                        lst3[h][l], lst3[h][l - 1] = lst3[h][l - 1], lst3[h][l]
        for h in range(l1):
            for m in range(k):
                if lst[h][m] != 0:
                    lst[h][m] = a / lst[h][m]
        answer = []
        for h in range(l1):
            w0 = 0
            w1 = 0
            w2 = 0
            for h in range(l1):
                for m in range(k):
                    if lst3[h][m] == 0:
                        w0 += lst[h][m]
                    if lst3[h][m] == 1:
                        w1 += lst[h][m]
                    if lst3[h][m] == 2:
                        w2 += lst[h][m]
            maxx = max(w0, w1, w2)
            ans = -1
            if maxx == w0:
                ans = 0
            if maxx == w1:
                ans = 1
            if maxx == w2:
                ans = 2
            answer.append(ans)
        q = []
        for h in range(l1):
            q.append([])
        for h in range(l1):
            q[h] = testData[h], answer[h]
        print(q)

A = splitData(X, 5)
B = splitData(Y, 5)

print(kNN(A, B, 115, distance1))
print(weighted_kNN(A, B, 110, distance1, 2))

