## Day06 - 函数和模块的使用

---

日期：2021年1月23日

今天是学习Python的第六天，按之前学校的C++教学进度来看，这学的还真是挺快的，今天看了一些简单的程序，也能看的懂了，大胆想象后面自己写一些东西出来的样子，还有点小期待。

学习用的教材是GitHub上骆昊编写的[《Python - 100天从新手到大师》](https://github.com/jackfrued/Python-100-Days)

所有编写的源代码均放在GitHub上：[https://github.com/svip886/Python_learning](https://github.com/svip886/Python_learning)

---

### 一、函数的作用


> 代码有很多种坏味道，重复是最坏的一种！ - Martin Fowler

函数的作用就是，解决代码重复使用的问题，将重复的代码封装在一个模块中，需要的时候可以直接调用。

### 二、定义函数

使用关键字`def`来定义函数

> 和C语言差不多，但是不需要区分“声明”和“返参”

求和函数例子：

```python
def sum1(a,b):
    return a+b
print(sum1(1,2))

def sum2(a,b):
    print(a+b)
sum2(1,2)
```

💡 实际上，Python的标准库已经有许多现成的函数可以直接调用，不需要自己多写一个求和函数，有违极简之道。

二、函数的参数

> Python对函数参数的处理与C++有一些区别，它支持使用可变参数，而不需要函数重载，可变参数只需在参数名前加个`*`号

多数求和：

```python
def add(*a): # a前加*号表示为可变参数
    s=0
    for n in a:
        s+=n
    return s

print(add(1,5.5,6,7))
```

### 三、用模块管理函数

> Python不支持函数的重载，所以在同一个py内，如果出现了同名函数，则后者将前者覆盖，这种情况很容易发生在多人协作完成一个项目。要解决这个问题，可以利用模块来管理函数

将函数写在其他py文件中，然后通过`import`或`from import`来调用，`as`可以修改为自定义名称，如下例子：

`foo1.py`

```python
def foo():
    print(1)
```

`foo2.py`

```python
def foo():
    print(2)
```

`main.py`

```python
import foo1 as f1
from foo2 import foo
f1.foo() # 1
foo() # 2
```

> 值得注意的是：如果导入的模块除了特定函数之外还有其他可执行代码，使用import导入之后也会执行这些代码，如果希望他只在直接运行该模块的时候执行这些代码，可以利用模块变量“__ name __”和直接执行模块名“ __ main __”。

`foo2.py`

```python
def foo():
    print(2)

if __name__ == '__main__': # 判断是否为直接运行的模块
    print('foo2被运行')
```

`mian.py`

```python
import foo2
```

### 四、练习

1. 实现计算求最大公约数和最小公倍数的函数。

    ```python
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
    ```

    💡 把公约数和公倍数分开之后，公约数的函数需要多运行一次，不知道会不会有更简单的方法，比如指针，后面学到再改良吧。

2. 实现判断一个数是不是回文数的函数。

    > 回文数就是，从左边开始读和从右边开始读是一样的数字，例如12321

    ```python
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
    ```

    💡 利用位提取来进行数字的翻转，再对比和原来是否一致，得出是否为回文数

3. 实现判断一个数是不是素数的函数。

    ```python
    from math import sqrt
    def is_prime(n):
        for x in range(2,int(sqrt(n)+1)):
            if n%x==0:
                return False
        return True if n!=1 else False # 代替三目运算符

    if __name__ = '__main__':
        n=int(input('n='))
        if is_prime(n):
            print('%d是素数' % (n))
        else:
            print('%d不是素数' % (n))
    ```

    💡 写过挺多遍判断素数了吧。。、值得一提的是，Python中没有三目运算符`?:`，但是可以用`if else`来替代，如代码里面所示。

4. 写一个程序判断输入的正整数是不是回文素数。

    ```python
    from test2 import is_palindrome
    from test3 import is_prime

    if __name__ == '__main__':
        n=int(input('n='))
        if is_prime(n) and is_palindrome(n):
            print('%d为回文素数' % (n))
        else:
            print('%d不是回文素数' % (n))
    ```

    💡 偷偷到练习2和练习3拿函数放一起，为避免拿来做模块后运行后面的可执行代码，加上模块名判断`if __name__ == '__main__'`

### 五、拓展：变量作用域

- 在函数中定义的变量，为局部变量，其只在函数里面有效，在函数外无法被调用，而函数则为该变量的作用域。

- 在所有封装外或分支结构中定义的变量，属于全局作用域。

- Python中，可以在定义函数中再定义函数，无限嵌套，暂且称为“子函数”。“子函数”可以访问调用“父函数”的变量，该变量就属于嵌套作用域；而“子函数”外无法访问内部的变量，“子函数”里的变量就属于局部作用域。

- 自带的标识符，如`int` `input` `print`，均属于内置作用域。

Python程序在运行过程中，会遵循一个变量作用域的顺序规则进行搜索：

**局部作用域→嵌套作用域→全局作用域→内置作用域**

所以，在实际开发中，应当尽量减少对全局变量的使用。因为全局变量的作用域和影响过于广泛，可能会发生意料之外的修改和使用，而且其生命周期比局部变量更长，可能会导致对象占用的内存长时间无法被释放。

> 所以，从先在开始，可以遵循一个代码书写规范，作为理解了函数和作用域基础上的一点改进

```python
def main():
    # Todo:Add your code here
    pass

if __name__ == '__main__':
    main()
```