import sys

sys.stdin=open('reduce.in','r')

sys.stdout=open('reduce.out','w')
ln=[]
for line in sys.stdin:
    ln.append(line.strip())
case=int(ln[0])
count=1
safety=0
while count <= case :
    i=count*2
    cow_n=int(ln[i-1])
    h=list(map(int,ln[i].strip().split()))
    hunger=[0]*(2*(cow_n)-1)
    for j in range(cow_n):
        hunger[j*2]=h[j]
    status=True
    k=0
    feed=0
    while k<cow_n-1:
        index=2*k+1
        try:
            if hunger[index-1]==hunger[index+1]:
                k+=1
                continue
            elif hunger[index-1]<hunger[index+1]:
                food=hunger[index+1]-hunger[index-1]
                hunger[index+2]+=(food)
                hunger[index+1]-=(food)
                hunger[index+3]-=(food)
                k+=1
            
            elif hunger[index-1]>hunger[index+1]:
                food=hunger[index-1]-hunger[index+1]
                
                if ((index+1)/2)%2!=0:
                    feed=-1
                    break
                else:
                    for m in range(int((index-1)/2)):
                        if m%2==0:
                            hunger[(2*m)+1]+=food
                            hunger[2*m]-=(food)
                            hunger[(2*m)+2]-=(food)
                        else:
                            continue
                k+=1   
        except:
            feed=-1
            break
        
        if k==cow_n-1 and hunger[0]!=hunger[cow_n*2-3]:
           k=0
        if min(hunger)<0:
            feed=-1 
            break
          
    #print(hunger)
    if feed!=-1:
        for l in range(cow_n-1):
            feed+=hunger[2*l+1]*2
    print(feed)
    count+=1
    






