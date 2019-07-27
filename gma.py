import sys,string,math
g1,g2=input().split()
m1=len(g1)
m2=len(g2)
if m2>m1:
    i=0
    while i<m1 and g1[i]==g2[i]:
        i+=1
      print(m2-i)
elif m2==m1:
    i=0
    while i<m2 and g1[i]==g2[i]:
        i+=1
     print(m2-i)
else:
    i=0
    while i<m2 and s1[i]==s2[i]:
        i+=1
  g35=g1[i:]
  g36=g2[i:]
  lt=list(g34)
  s=0
for v in s34:
    if v in lt:
        s+=1
        lt.remove(v)
 print(m1-1-v)   
        
    
