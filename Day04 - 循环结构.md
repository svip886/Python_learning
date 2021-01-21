## Day04 - 循环结构

---

日期：2021年1月21日

今天是学习Python的第四天，希望可以坚持下去。

学习用的教材是GitHub上骆昊编写的[《Python - 100天从新手到大师》](https://github.com/jackfrued/Python-100-Days)

所有编写的源代码均放在GitHub上：[https://github.com/svip886/Python_learning](https://github.com/svip886/Python_learning)

---

### 一、应用场景

同一个动作需要重复多次

### 二、for-in循环

> 适用场景：明确知道循环的次数

**求1-100的和**：

```python
sum=0
for x in range(101):
    sum+=x
print(sum)
```

💡 不只是if条件后需要加冒号“`:`”，只要是需要封装的函数体，都以冒号来作为起始标志，以缩进形式来表示其为函数体。

**`range()`的用法**：

- `range(101)`：表示0~100范围的整数，注意取不到101

- `range(1,100)`：表示1~100范围的整数，第一位参数为初值

- `range(1,101,2)`：表示1~100范围的奇数，第三位参数为步长。

- `range(100,0,-2)`：表示100~**1**的偶数。

💡 对于range的范围，可以看做是区间，左边为闭区间，右边为开区间

### 三、while循环

> 适用场景：不知道具体循环次数，达到条件后退出循环

示例：猜数字

```python
import random # 获取随机数字需要用到的库
answer=random.randint(1,100) # 取1~100随机数
x=0 # x需有初值，第一个while条件判断才不会出错
cout=0
while x!=answer:
    x=int(input('请输入数字:'))
    cout+=1
    if x>answer:
        print('太大了！')
    elif x<answer:
        print('太小了！')
    else:
        print('回答正确！你一共猜了%d次' % (cout))
if cout>7:
    print('你的智商明显不足') # 嘲讽
```
💡 Python中不支持c语言中的a++或者a--的语法，但支持+=这种。除了直接在while写循环条件外，也可以写成`while true`死循环，根据需要用`break`跳出循环。另外，`continue`在循环中，作用为结束本次循环，直接进入下一次循环。

### 四、循环的嵌套：

> 和C语言差不多，以九九乘法表为例

```python
for m in range(1,10):
    for n in range(1,m+1):
        print('%dx%d=%d' % (n,m,m*n),end='\t')
        # print默认以换行符结尾，end修改结束标志  
    print() # 加个换行符
```

💡 需要注意的是，**for** x **in** range(m,n)，一开始写忘记写`in`了。

### 五、练习

1. 输入一个正整数判断是不是素数

    > 素数为只能被1和自身整除的大于1的整数

    ```python
    from math import sqrt # 调用math中的sqrt函数求开方
    x=int(input('输入一个正整数：'))
    end=int(sqrt(x))
    is_prime=True
    for n in range(2,end+1):
        if x%n==0:
            is_prime=False
            break
    if is_prime and x!=1: # 1不是素数
        print('%d是素数' % (x))
    else:
        print('%d不是素数' % (x))
    ```
    
    💡 一开始的想法是从2到x-1能整除便不是素数，看完参考答案后发现，实际不用到x-1，这样多了很多没必要的计算，范围只需从2到sqrt(x)

2. 输入两个正整数，计算他们的最大公约数和最小公倍数

    ```python
    a=int(input('a='))
    b=int(input('b='))
    if a>b:
        a,b=b,a
    for factor in range(a,0,-1):
        if a%factor==0 and b%factor==0:
            break
    multiple=a*b/factor
    print('%d和%d的最大公约数为%d，最小公倍数为%d' % (a,b,factor,multiple))
    ```

    💡 看完参考答案后去掉了多余的变量，判断方式从递增改为递减，感觉做完练习后对我的思路很有帮助。

3. 打印三角形
   
   ```python
   row=int(input('请输入行数:'))
    # 右三角形
    for n in range(1,row+1):
        for x in range(n): 
            print('*',end='')
        print()
    # 左三角形
    for n in range(1,row+1):
        for x in range(row,0,-1):
            if x>n:
                print(' ',end='')
            else:
                print('*',end='')
        print()
    # 两边三角形
    for n in range(1,row+1):
        for x in range(row,n,-1):
                print(' ',end='')
        for y in range(1,2*n):
                print('*',end='')
        print()
   ```