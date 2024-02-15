import sys
import string
from collections import Counter

alphabets=Counter()
letters1,letters2={},{}
for a in list(string.ascii_lowercase):
    letters1[a],letters2[a]=0,0
l=[]
sys.stdin=open('blocks.in','r')
sys.stdout=open('blocks.out','w')

n=int(input())
board=[]
for i in range(n):
    board.append(list(input().strip().split()))

for i in board:
    alphabets=Counter(i[0])
#    print(alphabets)
    for j in alphabets.elements():
        if letters1[j]<alphabets[j]:
            letters1[j]=alphabets[j]
#    print(letters1)
    alphabets=Counter(i[1])
#    print(alphabets)
    for j in alphabets.elements():
        if letters1[j]<alphabets[j]:
            letters1[j]=alphabets[j]
#    print(letters1) 
    for k in letters1:
        letters2[k]+=letters1[k]
        letters1[k]=0
#    print(letters2)

for i in letters2:
    print(letters2[i])


