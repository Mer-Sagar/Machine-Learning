'''
===========================================================================================================
			*---*---*---*---*---*---*---*
			|       KNN Algorithm 	    |	
			*---*---*---*---*---*---*---*	
==========================================================================================================='''

bx=[3,2,5,2,1,3]
by=[2,4,6,1,3,2]

ox=[4,6,2,8,3,1]
oy=[7,5,3,5,2,4]
plt.scatter(bx, by)
plt.scatter(ox, oy)
k=int(input("Enter k for manthatten distance:-"))
xinput=int(input("Enter the x coordinate:-"))
yinput=int(input("Enter the y coordinate:- "))

plt.scatter(xinput,yinput)
plt.show()
dist=[]
for i in range (len(bx)):
    tmpList=[]
    tmpList.append(1)
    tmpList.append(abs(xinput-bx[i])+abs(yinput-by[i]))
    dist.append(tmpList)
        
for i in range (len(ox)):
    tmpList=[]
    tmpList.append(2)
    tmpList.append(abs(xinput-ox[i])+abs(yinput-oy[i]))
    dist.append(tmpList)
    dist.sort(key=lambda x:x[1])
print(dist)    

bcount=0
ocount=0
for i in range (k):
    if(dist[i][0]==1):
        bcount+=1
    elif(dist[i][0]==2):
        ocount+=1

if(bcount>ocount):
    print("Blue")
else:
    print("orange")

'''
===========================================================================================================
Output:
===========================================================================================================
Enter k for manthatten distance:-2
Enter the x coordinate:-6
Enter the y coordinate:- 6
[[1, 1], [2, 1], [2, 3], [2, 3], [1, 6], [1, 7], [1, 7], [2, 7], [2, 7], [2, 7], [1, 8], [1, 9]]
orange
'''