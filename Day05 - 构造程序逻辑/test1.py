"""
生成斐波那契数列的前20个数
特点：每个数都是它前面两个数的和
例如1，1，3，4，7，11，18，29，...
"""
a=int(input('a='))
b=int(input('b='))
print(a,b,end=' ')
for n in range(18):
    a+=b
    a,b=b,a
    print(b,end=' ')