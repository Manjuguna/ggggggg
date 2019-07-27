import sys, string, math
g1,g2 = input().split()
m1 = len(g1)
m2 = len(g2)
if m2 > m1 :
    i = 0
    while i<m1 and g1[i] == g2[i] :
        i += 1
    print(m2-i)
elif m2 == m1 :
    i = 0
    while i<m2 and g1[i] == g2[i] :
        i += 1
    print(m2-i)
else :

    i = 0
    while i<m2 and g1[i] == g2[i] :
        i += 1
    g31 = g1[i:]
    g32 = g2[i:]
    h = list(g31)
    k = 0
    for c in g32 :
        if c in h :
            k += 1
            h.remove(c)
    print(n1-i-k)
