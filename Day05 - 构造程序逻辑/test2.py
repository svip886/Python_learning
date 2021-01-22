"""
找出10000以内的完美数
所有因子（除本身外）加起来刚好等于本身
例如，6=1+2+3
"""

from math import sqrt
for n in range(2,10000):
    m=0
    for x in range(1,int(sqrt(n))+1):
        if n%x==0:
            m+=x
            if x!=n/x:
                m+=n/x
    if m==n:
        print(n)