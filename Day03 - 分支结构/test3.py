# 输入三条边长，如果能构成三角形就计算周长和面积。
# 三角形构成规则：两边之和大于打三边
# 海伦公式求面积

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and a+c>b and b+c>a:
    L=a+b+c
    p=L/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    print('构成的三角形周长为%.2f,面积为%.2f' % (L,S))
else:
    print('无法构成三角形')