import sys

sys.stdin=open('shell.in','r')

sys.stdout=open('shell.out','w')

ln=[]
for line in sys.stdin:
    ln.append(list(map(int,line.strip().split())))

score=0
point=0
case=ln[0][0]
for start in [1,2,3]:
    for i in range(case):
        swap1=ln[i+1][0]
        swap2=ln[i+1][1]
        guess=ln[i+1][2]
        
        
        if  start in [swap1,swap2] and start == swap1:
            start=swap2
        elif start in [swap1,swap2] and start==swap2:
            start=swap1
        if guess== start:
            score+=1
    if score>point:
        point=score
    score=0
print(point)
    
   



