import sys

sys.stdin=open('speeding.in','r')
sys.stdout=open('speeding.out','w')

n,m=map(int,input().strip().split())
road=[]
bessie=[]
for _ in range(n):
    road.append(list(map(int,input().strip().split())))

for _ in range(m):
    bessie.append(list(map(int,input().strip().split())))

segment=[[i+1] for i in range(100)]

j=0
k=0
for i in range(100):
    if i< road[j][0]:
        segment[i].append(road[j][1])
    if segment[i][0] == road[j][0] and i!=99:
        j+=1
        road[j][0]+=road[j-1][0]

    if i< bessie[k][0]:
        segment[i].append(bessie[k][1])
    if segment[i][0] == bessie[k][0] and i!=99:
        k+=1
        bessie[k][0]+=bessie[k-1][0]

overspeed=0
for _ in segment:
    if (_[2]-_[1])>overspeed:
        overspeed=(_[2]-_[1])

print(overspeed)

    
    

