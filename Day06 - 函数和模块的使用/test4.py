# 写一个程序判断输入的正整数是不是回文素数。

from test2 import is_palindrome
from test3 import is_prime

if __name__ == '__main__':
    n=int(input('n='))
    if is_prime(n) and is_palindrome(n):
        print('%d为回文素数' % (n))
    else:
        print('%d不是回文素数' % (n))