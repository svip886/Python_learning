# 实现判断一个数是不是回文数的函数。
# 回文数就是，从左边开始读和从右边开始读是一样的数字，例如12321
def is_palindrome(n):
    x=n
    re=0
    while x>0:
        re=re*10+x%10
        x//=10
    return re==n

if __name__ == '__main__':
    n=int(input('输入一个数字：'))
    if is_palindrome(n):
        print('%d为回文数' % (n))
    else:
        print('%d不是回文数' % (n))