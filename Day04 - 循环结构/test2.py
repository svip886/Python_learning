# 输入两个正整数，计算他们的最大公约数和最小公倍数

a=int(input('a='))
b=int(input('b='))
if a>b:
    a,b=b,a
for factor in range(a,0,-1):
    if a%factor==0 and b%factor==0:
        break
multiple=a*b/factor
print('%d和%d的最大公约数为%d，最小公倍数为%d' % (a,b,factor,multiple))
