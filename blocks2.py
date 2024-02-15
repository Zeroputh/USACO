import sys
import string

letters={}
for a in list(string.ascii_lowercase):
    letters[a]=0
sys.stdin=open('blocks.in','r')
sys.stdout=open('blocks.out','w')

n=int(input())
for i in range(n):
    board1,board2=input().strip().split()
    for j in letters:
        letters[j]+=max(board1.count(j),board2.count(j))


for i in letters:
    print(letters[i])


