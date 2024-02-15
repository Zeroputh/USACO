import sys

sys.stdin=open('mixmilk.in','r')
sys.stdout=open('mixmilk.out','w')

i=0
a=[0]*4
b=[0]*4
for line in sys.stdin:
    a[i],b[i]=map(int,line.strip().split())
    i+=1
a[3],b[3]=a[0],b[0]
count=0
i=0
while count<100:
    b[i+1]+=b[i]
    if(b[i+1]>a[i+1]):
        b[i]=b[i+1]-a[i+1]
        b[i+1]-=b[i]
    else:
        b[i]=0
    i+=1
    count+=1
    if i==3:
        b[0]=b[3]
        i=0
    b[3]=b[0]

for j in b[:3]:
    print(j)



