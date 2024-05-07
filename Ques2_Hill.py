from copy import deepcopy

def disp(a):
  i=0
  while i<7:
    print(a[i]," ",a[i+1]," ",a[i+2])
    i=i+3
  print(" ")


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
fin=[1,2,3,8,0,4,7,6,5]
open=[]
closed=[]
cur=ini
curheu=heu(cur)
open.append([cur,None,heu(cur)])
while heu(cur)!=0 or open==None:
  flag=True
  temo=open.pop(0)
  cur=temo[0]
  disp(cur)
  closed.append(temo)
  n=find(cur)+1
  if(n%3!=0 and flag==True):
    temc=right(cur)
    if(heu(temc)<curheu):
      open.append([temc,cur,heu(temc)])
      flag=False
  if(n%3!=1 and flag==True):
    temc=left(cur)
    if(heu(temc)<curheu):
      open.append([temc,cur,heu(temc)])
      flag=False
  if(n>3 and flag==True):
    temc=up(cur)
    if(heu(temc)<curheu):
      open.append([temc,cur,heu(temc)])
      flag=False
  if(n<7 and flag==True):
    temc=down(cur)
    if(heu(temc)<curheu):
      open.append([temc,cur,heu(temc)])
      flag=False
  curheu=heu(cur)