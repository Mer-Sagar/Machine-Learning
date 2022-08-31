'''
===========================================================================================================
			*---*---*---*---*---*---*---*
			|	Fuzzy Kmeans Algorithm	|	
			*---*---*---*---*---*---*---*	
==========================================================================================================='''

from matplotlib import pyplot as plt

def manhattenDistace(v1, v2):
    return abs(v1[0]-v2[0])+abs(v1[1]-v2[1])

def findMembershipValues(ele, centroids):
    membershipValues = []
    for cent1 in centroids:
        sum = 0
        if(manhattenDistace(ele, cent1) == 0):
            sum = 1
        else:
            for cent2 in centroids:
                if(manhattenDistace(ele, cent2) == 0):
                    sum = 0
                    break
                else:
                    sum += pow(manhattenDistace(ele, cent1), 2) / \
                        pow(manhattenDistace(ele, cent2), 2)
        if(sum == 0):
            membershipValues.append(0)
        else:
            membershipValues.append(1/sum)
    return membershipValues

data = [[3, 4], [5, 6], [1, 3], [4, 3], [7, 7],
        [2, 3], [7, 8], [2, 1], [4, 2], [7, 3]]

k = int(input("Enter value of k:"))
centroids = [data[i] for i in range(k)]
while True:
    clusters = [[] for i in range(k)]
    membershipValues = []
    for ele in data:
        membershipValues.append(findMembershipValues(ele, centroids))
    newcentroid = []
    for i in range(len(membershipValues[0])):
        xcent = 0
        ycent = 0
        sum = 0
        for j in range(len(membershipValues)):
            xcent += data[j][0]*pow(membershipValues[j][i], 2)
            ycent += data[j][1]*pow(membershipValues[j][i], 2)
            sum += pow(membershipValues[j][i], 2)
        newcentroid.append([xcent/sum, ycent/sum])
    
    sum = 0
    for i in range(len(newcentroid)):
        sum += (abs(newcentroid[i][0]-centroids[i][0]) +
                abs(newcentroid[i][1]-centroids[i][1]))
    
    if int(sum) == 0:
        break
    else:
        centroids = newcentroid
for i in range(len(data)):
    print(data[i], membershipValues[i])

'''
===========================================================================================================
Output:
===========================================================================================================
Enter value of k:3
[3, 4] [0.6199769729137763, 0.05813467198386606, 0.3218883551023577]
[5, 6] [0.2242820872937004, 0.6966937306558824, 0.07902418205041718]
[1, 3] [0.17563997003718734, 0.01915446281755015, 0.8052055671452625]
[4, 3] [0.9986689892784277, 0.00020361363967572727, 0.001127397081896555]
[7, 7] [0.011739836587036324, 0.9821758317551287, 0.006084331657834821]
[2, 3] [0.0912214097935389, 0.005653829502063303, 0.9031247607043977]
[7, 8] [0.045536473128679464, 0.9291081325409156, 0.025355394330404908]
[2, 1] [0.1286157916298566, 0.020132341127186985, 0.8512518672429564]
[4, 2] [0.8322647016810002, 0.018831489221237906, 0.14890380909776182]
[7, 3] [0.5589177286377318, 0.27412315498176587, 0.1669591163805024]
'''