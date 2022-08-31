'''
===========================================================================================================
			*---*---*---*---*---*---*---*
			|       K Means alogorithm  |	
			*---*---*---*---*---*---*---*		
==========================================================================================================='''

from matplotlib import pyplot as plt 

def manhattenDistance(v1,v2):
    return abs(v1[0]-v2[0])+abs(v1[1]-v2[1])

def makeClusters(ele,centroids):
    dist=[]
    for centroid in centroids:
        dist.append(manhattenDistance(ele,centroid))
    return dist.index(min(dist))

def newCentroids(clusters):
    print(clusters)
    sumx=0
    sumy=0
    newCentroid=[]
    for idx in range(len(clusters)):
        sumx=0
        sumy=0
        new_centroids=[]
        for i in range(len(clusters[idx])):
            sumx+=clusters[idx][i][0]
            sumy+=clusters[idx][i][1]
        xavg=sumx/len(clusters[idx])
        yavg=sumy/len(clusters[idx])
        new_centroids.append(xavg)
        new_centroids.append(yavg)
        newCentroid.append(new_centroids)
    return newCentroid

data=[[2,5],[1,2],[5,4],[2,3],[1,4],[5,7],[7,8],[6,6],[6,4],[3,2],[4,6]]
x=[data[i][0] for i in range(len(data))]
y=[data[i][1] for i in range(len(data))]

k=int(input("Enter value of k:"))
centroids=[data[i] for i in range(k)]
print(centroids)

while True:
    clusters=[[] for i in range(k)]
    for ele in data:
        idx=makeClusters(ele,centroids)
        clusters[idx].append(ele)
    newCentroid=newCentroids(clusters)
    print(newCentroid)
    sumofCent=0
    for idx in range(len(centroids)):
        sumofCent+=abs(centroids[idx][0]-newCentroid[idx][0])+abs(centroids[idx][1]-newCentroid[idx][1])
    print(sumofCent)
    if(sumofCent==0):
        break
    else:
        centroids=newCentroid
i=0
for cluster in clusters:
    print(f"Cluster {i+1}:",cluster)
    i+=1
plt.scatter(x,y)
plt.show()

'''
===========================================================================================================
Output:
===========================================================================================================

Enter value of k:3
[[2, 5], [1, 2], [5, 4]]
[[[2, 5], [2, 3], [1, 4], [4, 6]], [[1, 2], [3, 2]], [[5, 4], [5, 7], [7, 8], [6, 6], [6, 4]]]
[[2.25, 4.5], [2.0, 2.0], [5.8, 5.8]]
4.35

[[[2, 5], [1, 4]], [[1, 2], [2, 3], [3, 2]], [[5, 4], [5, 7], [7, 8], [6, 6], [6, 4], [4, 6]]]
[[1.5, 4.5], [2.0, 2.3333333333333335], [5.5, 5.833333333333333]]
1.4166666666666665

[[[2, 5], [1, 4]], [[1, 2], [2, 3], [3, 2]], [[5, 4], [5, 7], [7, 8], [6, 6], [6, 4], [4, 6]]]
[[1.5, 4.5], [2.0, 2.3333333333333335], [5.5, 5.833333333333333]]
0.0

Cluster 1: [[2, 5], [1, 4]]
Cluster 2: [[1, 2], [2, 3], [3, 2]]
Cluster 3: [[5, 4], [5, 7], [7, 8], [6, 6], [6, 4], [4, 6]]
'''