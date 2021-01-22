## Day05 - 构造程序逻辑

---

日期：2021年1月22日

今天是学习Python的第五天，前四天的学习已经可以构建基本简单程序来解决一些现实问题了，今天的目标是通过一些典型例子来巩固前面的知识,以前学C的时候就写过了，只是换了Python来写。

学习用的教材是GitHub上骆昊编写的[《Python - 100天从新手到大师》](https://github.com/jackfrued/Python-100-Days)

所有编写的源代码均放在GitHub上：[https://github.com/svip886/Python_learning](https://github.com/svip886/Python_learning)

---

### 一、寻找水仙花数

> 水仙花数为3为数，其每个位上数字的立方和等于它本身。eg：1³+5³+3³=153

```python
for n in range(100,1000): # 范围三位数
    if (n%10)**3+(n//10%10)**3+(n//100%10)**3==n:
        print(n)
```

💡 一开始print不回显，调试后发现取百位和十位的时候有小数，将/换成//整除，就解决了。

**拓展：正整数反转**

> 利用求位运算来实现

```python
num=int(input('输入一个正整数：'))
reversed_num=0
while num>0:
    reversed_num=reversed_num*10+num%10
    num//=10
print(reversed_num)
```

### 二、百钱白鸡问题

> 公鸡5元/只，母鸡3元/只，小鸡1元/3只，用100元买一百只鸡，怎么分配

```python
for x in range(0,20):
    for y in range(0,33):
        z=100-x-y
        if 5*x+3*y+z/3==100:
            print('公鸡%d只，母鸡%d只，小鸡%d只' % (x,y,z))
```

### 三、CRAPS赌博游戏

> 骰子游戏。游戏规则：玩家投2个骰子，第一次摇到7、11点，玩家胜；第一次摇到2、3、12点，庄家胜；其他点数继续摇，摇到7点，庄家胜，摇到第一次的点数，玩家胜，直至分出胜负。

```python
from random import randint
money=1000 # 初始金额
while money>0:
    print('当前资产为%d元' % (money))
    while True:
        x=int(input('请下注：'))
        if x>0 and x<=money:
            print('游戏开始！')
            break
        else:
            print('下注金额不在可用金额范围内，请重新输入！')
    input('按回车键开始摇骰子')
    first=randint(1,6)+randint(1,6)
    print('你摇出了%d点' % (first))
    if first==7 or first==11:
        print('你赢了！')
        money+=x
    elif first==2 or first==3 or first==12:
        print('你输了！')
        money-=x
    else:
        while True:
            input('按回车键开始摇骰子')
            again=randint(1,6)+randint(1,6)
            print('你摇出了%d点' % (again))
            if again==first:
                print('你赢了！')
                money+=x
                break
            elif again==7:
                print('你输了！')
                money-=x
                break
            else:
                print('再来一次') 
print('你没钱了，输的只剩一条内裤~')
```

### 四、练习

1. 生成斐波那契数列的前20个数

    > 特点：每个数都是它前面两个数的和，例如1，1，3，4，7，11，18，29，

    ```python
    a=int(input('a='))
    b=int(input('b='))
    print(a,b,end=' ')
    for n in range(18):
        a+=b
        a,b=b,a
        print(b,end=' ')
    ```
2. 找出10000以内的完美数

    > 完美数：所有因子（除本身外）加起来刚好等于本身.例如，6=1+2+3

    ```python
    from math import sqrt
    for n in range(2,10000):
        m=0
        for x in range(1,int(sqrt(n))+1):
            if n%x==0:
                m+=x
                if x!=n/x and x>1:
                    m+=n/x
        if m==n:
            print(n)
    ```

3. 找出100以内所有的素数

    ```python
    from math import sqrt
    for n in range(2,100):
        is_prime=True
        for factor in range(2,int(sqrt(n)+1)):
            if n%factor==0:
                is_prime=False
                break
        if is_prime:
            print(n,end=' ')
    ```