import sys
import itertools
import string
from collections import Counter

alphabets=Counter()
letters={}
for a in list(string.ascii_lowercase):
    letters[a]=0
l=[]
sys.stdin=open('blocks.in','r')
sys.stdout=open('blocks.out','w')

n=int(input())
board=[]
for i in range(n):
    board.append(list(input().strip().split()))

prod=[]
prod=itertools.product(*board)



for _ in prod:
    for __ in _:
       alphabets.update(__)
    l.append(alphabets)
    alphabets=Counter()


for i in letters:
    for j in l:
        try:
            if letters[i]<j[i]:
                letters[i]=j[i]
        except:
            continue



for t in letters.values():
    print(t)