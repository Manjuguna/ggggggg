import sys, string, math
da1,da2 = input().split()
ms1 = len(da1)
ms2 = len(da2)
if ms2 > ms1 :
    i = 0
    while i<ms1 and da1[i] == da2[i] :
        i += 1
    print(ms2-i)
elif ms2 == ms1 :
    i = 0
    while i<ms2 and da1[i] == da2[i] :
        i += 1
    print(ms2-i)
else :

    i = 0
    while i<ms2 and da1[i] == da2[i] :
        i += 1
    da31 = da1[i:]
    da32 = da2[i:]
    gt = list(da31)
    gm = 0
    for cn in da32 :
        if cn in gt :
            gm += 1
            gt.remove(cn)
    print(ms1-i-gm)
