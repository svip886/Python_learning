"""
找出100以内所有的素数


"""

from math import sqrt
for n in range(2,100):
    is_prime=True
    for factor in range(2,int(sqrt(n)+1)):
        if n%factor==0:
            is_prime=False
            break
    if is_prime:
        print(n,end=' ')