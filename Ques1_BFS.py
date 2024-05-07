from copy import deepcopy

def disp(a):
  i=0
  while i<7:
    print(a[i]," ",a[i+1]," ",a[i+2])
    i=i+3
  print(" ")

def sorth(sa):
  si=0
  while si<len(sa):
    sj=0
    while sj<len(sa)-1:
      if(sa[sj][2]>sa[sj+1][2]):
        stemp=sa[sj]
        sa[sj]=sa[sj+1]
        sa[sj+1]=stemp
      sj=sj+1
    si=si+1

def find(fa):
  fi=0
  while fi<9:
    if(fa[fi]==0):
      return fi
    fi=fi+1

def left(b):
  n=find(b)
  a=deepcopy(b)
  temp=a[n]
  a[n]=a[n-1]
  a[n-1]=temp
  return a

def right(b):
  n=find(b)
  a=deepcopy(b)
  temp=a[n]
  a[n]=a[n+1]
  a[n+1]=temp
  return a

def up(b):
  n=find(b)
  a=deepcopy(b)
  temp=a[n]
  a[n]=a[n-3]
  a[n-3]=temp
  return a

def down(b):
  n=find(b)
  a=deepcopy(b)
  temp=a[n]
  a[n]=a[n+3]
  a[n+3]=temp
  return a

def heu(a):
  i=0
  h=0
  while i<9:
    if(a[i]!=0):
      if(a[i]!=fin[i]):
        h=h+1
    i=i+1
  return h

ini=[2,0,3,1,8,4,7,6,5]
fin=[1,2,3,8,0,4,7,6,5,]
open=[]
closed=[]
cur=ini
open.append([cur,None,None])
while heu(cur)!=0 or open==None:
  temo=open.pop(0)
  cur=temo[0]
  disp(cur)
  closed.append(temo)
  n=find(cur)+1
  if(n%3!=0):
    temc=right(cur)
    open.append([temc,cur,heu(temc)])
  if(n%3!=1):
    temc=left(cur)
    open.append([temc,cur,heu(temc)])
  if(n>3):
    temc=up(cur)
    open.append([temc,cur,heu(temc)])
  if(n<7):
    temc=down(cur)
    open.append([temc,cur,heu(temc)])
  sorth(open)