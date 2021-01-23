# 实现判断一个数是不是素数的函数。

from math import sqrt
def is_prime(n):
    for x in range(2,int(sqrt(n)+1)):
        if n%x==0:
            return False
    return True if n!=1 else False # 代替三目运算符

if __name__ == '__main__':
    n=int(input('n='))
    if is_prime(n):
        print('%d是素数' % (n))
    else:
        print('%d不是素数' % (n))