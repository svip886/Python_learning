## Day03 - 分支结构

今天是学习Python的第三天，希望可以坚持下去。

学习用的教材是GitHub上骆昊编写的[《Python - 100天从新手到大师》](https://github.com/jackfrued/Python-100-Days)

所有编写的源代码均放在GitHub上：[https://github.com/svip886/Python_learning](https://github.com/svip886/Python_learning)

### 一、应用场景

需要根据情况不同来执行不同的程序，这种结构称为“分支结构”或“选择结构”。

### 二、if判断语句的使用

> 和C语言一样，关键字为`if`和`else`，不同在于使用规范不一样，在Python中，一般括起来的函数体是以缩进（使用Tab或者四个空格）来表示的，条件后需要加个冒号“`:`”。

```python
# 身份验证
username=input('请输入用户名：')
password=input('请输入密码：')
if username=='admin' and password=='123456': # 判断条件
    print('登录成功！') # 正确
else: # 判断条件不成立
    print('请检查你的用户名和密码！') # 错误
```

💡`else if`可以简写为`elif`，可以让代码看起来更简洁，扁平化。

### 三、拓展

> Python中没有C语言中的switch结构，在网上找到了代替方案

```python
def case1(somearg):
    pass
def case2(somearg):
    pass
def case3(somearg):
    pass
switch={
1: case1,
2: case2,
3: case3
}
switch[case](arg)
```

💡感觉更复杂了，有违Python的极简之道，其实用`elif`也可以让分支结构容易看，那switch可能就没有那么必要了。

### 四、练习

1. 英制单位英寸和公制单位厘米互换。

    ```python
    # 1英寸=2.54厘米

    l=float(input('请输入需要转换的长度：'))
    unit=input('请输入单位：')
    if unit=='in' or unit=='英寸':
        print('%.2f英寸 = %.2f厘米' % (l,l*2.54))
    elif unit=='cm' or unit=='厘米':
        print('%.2f厘米 = %.2f英寸' % (l,l/2.54))
    else:
        print('请输入正确的单位！')
    ```

2. 百分制成绩转换为等级制成绩。

    ```python
    # A:score≥90|B:80≤score<90|C:70≤score<80|D：60≤score<70|E：score<60

    score=float(input('输入分数：'))
    if score>=0 and score<=100: # 判断输入是否符合百分制
        if score>=90:
            grade='A'
        elif score>=80:
            grade='B'
        elif score>=70:
            grade='C'
        elif score>=60:
            grade='D'
        else:
            grade='E'
        print('该分数等级为:',grade)
    else:
        print('分数输入错误，请重新输入！')
    ```

    💡print可以像C++的输出cout一样，使用拼接的方式。

3. 输入三条边长，如果能构成三角形就计算周长和面积。

    ```python
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
    ```

    💡海伦公式：$S=\sqrt{p(p-a)(p-b)(p-c)}$
    
    - 其中p为半周长