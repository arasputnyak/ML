import copy
import math, random
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

def cross_validation(data_X, data_Y, k, kNN, neir, distance):
    errors = []
    test_train_data_X = splitData(data_X, k)
    test_train_data_Y = splitData(data_Y, k)
    classes = kNN(test_train_data_X, test_train_data_Y, neir, distance)
    for i in range(k):
        #trainData = test_train_data_X[i][0]
        #testData = test_train_data_X[i][1]
        #tr_Y = test_train_data_Y[i][0]
        ts_Y = test_train_data_Y[i][1]
        err = 0
        for j in range(len(ts_Y)):
            if ts_Y[j] != classes[i][j]:
                err += 1
        err = err / len(ts_Y)
        errors.append(err)
    return sum(errors) / k

def num_of_elem(lst, elem, k):
    count = 0
    for i in range(k):
        if lst[i] == elem:
            count +=1
    return count

def kNN(test_train_data_X, test_train_data_Y, k, distance):
    godwhy = []
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
        godwhy.append(answer)
        #q = []
        #for h in range(l1):
            #q.append([])
        #for h in range(l1):
            #q[h] = testData[h], answer[h]
        #print(q)
    return godwhy

def weighted_kNN(test_train_data_X, test_train_data_Y, k, distance):
    godwhy = []
    lst = []
    lst2 = []
    lst3 = []
    a = 2
    #a = random.randint(1, 5)
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
        godwhy.append(answer)
        # q = []
        # for h in range(l1):
        # q.append([])
        # for h in range(l1):
        # q[h] = testData[h], answer[h]
        # print(q)
    return godwhy

#A = splitData(X, 5)
#B = splitData(Y, 5)

#print(kNN(A, B, 115, distance1))
#print(weighted_kNN(A, B, 110, distance1, 2))
#print(cross_validation(X, Y, 5, kNN, 115, distance1))
#print(cross_validation(X, Y, 3, weighted_kNN, 90, distance1))
