import sys
from itertools import combinations
ar=40000*40000
sys.stdin=open("reduce.in","r")
file=open("reduce.in","r")

sys.stdout=open("reduce.out","w")
list1=[]
for _ in range(int(input())):
    list1.append(tuple(map(int,input().strip().split())))

minx,maxx,miny,maxy=[],[],[],[]

minx=sorted(list1,key=lambda x:x[0])[:4]
maxx=sorted(list1,key=lambda x:x[0],reverse=True)[:4]
miny=sorted(list1,key=lambda x:x[1])[:4]
maxy=sorted(list1,key=lambda x:x[1],reverse=True)[:4]


def minmax(list2):
    minx=sorted(list2,key=lambda x:x[0])[:4]
    maxx=sorted(list2,key=lambda x:x[0],reverse=True)[:4]
    miny=sorted(list2,key=lambda x:x[1])[:3]
    maxy=sorted(list2,key=lambda x:x[1],reverse=True)[:4]
    return([maxx[0],minx[0],maxy[0],miny[0]])

def area(x):
    a=(x[0][0]-x[1][0])*(x[2][1]-x[3][1])
    return a 

comb=minx+maxx+miny+maxy
extreme=list(set(comb))


removed=list(combinations(extreme,3))
for i in list(removed):
    temp=extreme[:]
    
    for j in i:
        try:
            temp.remove(j)
        except:
            continue
    t=area(minmax(temp))
    if t<ar:
        ar=t

print(ar)    

    






            


