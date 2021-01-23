# 实现计算求最大公约数和最小公倍数的函数。

def max_factor(a,b):
    if a>b:
        a,b=b,a
    for factor in range(a,0,-1):
        if a%factor==0 and b%factor==0:
            break
    return factor
def min_multiple(a,b):
    return a*b/max_factor(a,b)


a=int(input('a='))
b=int(input('a='))
print('最大公约数：%d，最小公倍数：%d' % (max_factor(a,b),min_multiple(a,b)))
