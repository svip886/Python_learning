# 输入一个正整数判断是不是素数

from math import sqrt # 调用math中的sqrt函数求开方
x=int(input('输入一个正整数：'))
end=int(sqrt(x))
is_prime=True
for n in range(2,end+1):
    if x%n==0:
        is_prime=False
        break
if is_prime and end!=1: # 1不是素数
    print('%d是素数' % (x))
else:
    print('%d不是素数' % (x))