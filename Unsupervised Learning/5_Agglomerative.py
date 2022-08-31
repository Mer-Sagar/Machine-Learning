'''
===========================================================================================================
			*---*---*---*---*---*---*---*
			|   Agglomerative Algorithm |	
			*---*---*---*---*---*---*---*	
==========================================================================================================='''

import pandas as pd
from numpy import array
def agglomerative(data, k):
    cluster = []
    for x in data:
        innercluster = []
        innercluster.append(x)
        cluster.append(x)
    while(len(data) > k):
        min = distance(data[0], data[1])
        merge = [0, 1]
        for i in range(len(data)):
            for j in range((i+1), len(data)):
                dist = distance(data[i], data[j])
                if dist < min and dist != 0:
                    min = dist
                    merge = [i, j]

        newData = []
        for x in range(len(merge)):
            newData.append(data[merge[x]])
        data[merge[0]] = newData
        data.pop(merge[1])
        print(data)

def centroid(x):
    if(type(x[0]) == type(x[0][0])):
        x = all_in_one(x)
    total = [0]*2
    for i in x:
        for j in range(len(i)):
            total[j] += i[j]
    for i in range(len(total)):
        total[i] = total[i]/len(x)
    return total


def all_in_one(x):
    data = []
    for i in x:
        if type(i) == type(i[0]):
            data.extend(all_in_one(i))
        else:
            data.append(i)
    return data

def distance(x, y):
    if(type(x) == type(x[0])):
        a = centroid(x)
    else:
        a = x
    if(type(y) == type(y[0])):
        b = centroid(y)
    else:
        b = y

    total = 0
    for x in range(len(a)):
        total += (abs(a[x]-b[x]))
    return total

data = [[5, 3], [4, 1], [2, 6], [5, 7], [3, 7], [9, 4], [3, 6]]
k = int(input("Enter the k value:"))
agglomerative(data, k)

'''
===========================================================================================================
Output:
===========================================================================================================
Enter the k value:3
[[5, 3], [4, 1], [[2, 6], [3, 6]], [5, 7], [3, 7], [9, 4]]
[[5, 3], [4, 1], [[[2, 6], [3, 6]], [3, 7]], [5, 7], [9, 4]]
[[[5, 3], [4, 1]], [[[2, 6], [3, 6]], [3, 7]], [5, 7], [9, 4]]
[[[5, 3], [4, 1]], [[[[2, 6], [3, 6]], [3, 7]], [5, 7]], [9, 4]]
'''